from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
# LISTS
import core.constants.states as states
import core.constants.breed_list as breed_list
import core.constants.age_list as age_list
import core.constants.policy_limit_factor_list as policy_limit_factor_list

import uuid

import datetime
from dateutil.relativedelta import *

from model_utils import Choices


def next_year():
    """Return the next year from the purches date"""
    startDate = datetime.date.today()
    endDate = startDate.replace(startDate.year + 1)
    return f'{endDate}'

def payment_list():
    """A list with all the difrrent dates"""
    startDate = datetime.date.today()
    PAYMENT_LIST = [
        f'{startDate+relativedelta(months=+1)}',
        f'{startDate+relativedelta(months=+2)}',
        f'{startDate+relativedelta(months=+3)}',
        f'{startDate+relativedelta(months=+4)}',
        f'{startDate+relativedelta(months=+5)}',
        ]
    return PAYMENT_LIST
    # MONTHS_LIST = Choices(
    #     (0, '1', _(dateM.replace(dateM.month + 1))),
    # )


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and save a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    # Customer importand information
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Other infromation
    phone_number = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        default='0000000000'
    )
    address_1 = models.CharField(
        max_length=255,
        default='',
        null=False,
        blank=False
    )
    address_2 = models.CharField(
        max_length=255,
        default='',
        null=False,
        blank=False
    )
    city = models.CharField(
        max_length=255,
        default='',
        null=False,
        blank=False
    )
    zipcode = models.CharField(
        max_length=5,
        null=False,
        blank=False,
        default='00000'
    )
    state = models.CharField(
        blank=True,
        max_length=2,
        choices=states.STATE_CHOICES
    )
    paid_until = models.DateTimeField(
        null=True,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Plan(models.Model):
    """A single plan for a single user"""
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'), blank=True)
    default = models.BooleanField(
        null=True,
        help_text=_('Both "Unknown" and "No" means that the plan is not default'),
        default=None,
        db_index=True,
        unique=True,
    )
    available = models.BooleanField(
        _('available'), default=False, db_index=True,
        help_text=_('Is still available for purchase')
    )
    visible = models.BooleanField(
        _('visible'), default=True, db_index=True,
        help_text=_('Is visible in current offer')
    )
    created = models.DateTimeField(_('created'), db_index=True)
    customized = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        verbose_name=_('customized'),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class PaymentList(models.Model):
    """List of payments dates"""
    paymentList_id = models.CharField(
        max_length=255,
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        blank=False,
        null=False,
    )
    myList = models.TextField(null=True, default=payment_list)

    def __str__(self):
        return self.paymentList_id


class UserPlan(models.Model):
    """Currently selected plan for user account"""
    userPlan_id = models.CharField(
        max_length=255,
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        blank=False,
        null=False,
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name=_('user'),
        on_delete=models.CASCADE
    )
    plan = models.ForeignKey('Plan', verbose_name=_('plan'), on_delete=models.CASCADE)
    expire = models.DateField(
        _('expire'), default=next_year, blank=True, null=True, db_index=True)
    active = models.BooleanField(_('active'), default=True, db_index=True)
    payment_list = models.ForeignKey('PaymentList', default=datetime.date.today(), verbose_name=_('payment list'), on_delete=models.CASCADE)

    def __str__(self):
        return self.userPlan_id

    def is_active(self):
        return self.active

    def expire_date(self):
        return date.today() - self.DOB.year

    def is_expired(self):
        if self.expire is None:
            return False
        else:
            return self.expire < date.today()

    def days_left(self):
        if self.expire is None:
            return None
        else:
            return (self.expire - date.today()).days

    def clean_activation(self):
        errors = plan_validation(self.user)
        if not errors['required_to_activate']:
            plan_validation(self.user, on_activation=True)
            self.activate()
        else:
            self.deactivate()
        return errors

    def activate(self):
        if not self.active:
            self.active = True
            self.save()
            account_activated.send(sender=self, user=self.user)

    def deactivate(self):
        if self.active:
            self.active = False
            self.save()
            account_deactivated.send(sender=self, user=self.user)

    def initialize(self):
        """
        Set up user plan for first use
        """
        if not self.is_active():
            # Plans without pricings don't need to expire
            if self.expire is None and self.plan.planpricing_set.count():
                self.expire = now() + timedelta(
                    days=getattr(settings, 'PLANS_DEFAULT_GRACE_PERIOD', 30))
            self.activate()  # this will call self.save()

    @classmethod
    def create_for_user(cls, user):
        default_plan = Plan.get_default_plan()
        if default_plan is not None:
            return UserPlan.objects.create(
                user=user,
                plan=default_plan,
                active=False,
                expire=None,
            )

    @classmethod
    def create_for_users_without_plan(cls):
        userplans = get_user_model().objects.filter(userplan=None)
        for user in userplans:
            UserPlan.create_for_user(user)
        return userplans

    def get_current_plan(self):
        """ Tiny helper, very usefull in templates """
        return Plan.get_current_plan(self.user)
