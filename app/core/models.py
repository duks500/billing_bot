from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
# LISTS
import core.constants.states as states
import core.constants.breed_list as breed_list
import core.constants.age_list as age_list
import core.constants.policy_limit_factor_list as policy_limit_factor_list

import uuid

import datetime
from dateutil.relativedelta import relativedelta

from model_utils import Choices


def next_year():
    """Return the next year from the purches date"""
    startDate = datetime.date.today()
    endDate = startDate.replace(startDate.year + 1)
    return f'{endDate}'


def payment_list():
    """A list with all the difrrent dates"""
    startDate = datetime.date.today()
    # startDate = startDate+relativedelta(day=+31)
    PAYMENT_LIST = [
        f'{startDate+relativedelta(months=+1)}',
        f'{startDate+relativedelta(months=+2)}',
        f'{startDate+relativedelta(months=+3)}',
        f'{startDate+relativedelta(months=+4)}',
        f'{startDate+relativedelta(months=+5)}',
        f'{startDate+relativedelta(months=+6)}',
        f'{startDate+relativedelta(months=+7)}',
        f'{startDate+relativedelta(months=+8)}',
        f'{startDate+relativedelta(months=+9)}',
        f'{startDate+relativedelta(months=+10)}',
        f'{startDate+relativedelta(months=+11)}',
        ]
    return PAYMENT_LIST


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
    token_oneinc = models.CharField(
        null=True,
        max_length=255,
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'


class Quote(models.Model):
    """Quote to be assign to user later on"""
    GENDER_LIST = Choices(
        ('Cat', ['Male', 'Female']),
        ('Dog', ['Male', 'Female'])
    )
    BREEDING_ENDORSEMENT_LIST = Choices(
        ('No'),
        ('Male'),
        ('Female')
    )
    RECURRENCE_LIST = Choices(
        ('Monthly'),
        ('Yearly')
    )

    quote_id = models.CharField(
        max_length=255,
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        blank=False,
        null=False,
    )
    pet_name = models.CharField(
        max_length=255,
        default='MAX'
    )
    base_rate = models.DecimalField(
        default=54.11,
        max_digits=4,
        decimal_places=2
    )
    geographical_factor = models.DecimalField(
        default=0,
        max_digits=4,
        decimal_places=2
    )
    gender_factor = models.CharField(
        blank=True,
        max_length=6,
        choices=GENDER_LIST,
    )
    breed_factor = models.CharField(
        blank=True,
        max_length=255,
        choices=breed_list.BREED_LIST
    )
    age_factor = models.CharField(
        blank=True,
        max_length=255,
        choices=age_list.AGE_LIST
    )
    policy_limit_factor = models.CharField(
        blank=True,
        max_length=255,
        choices=policy_limit_factor_list.POLICY_LIMIT_FACTOR_LIST
    )
    deductibale_factor = models.PositiveIntegerField(
        default=500
    )
    coinsurance_factor = models.PositiveIntegerField(
        default=50,
    )
    exam_fee_factor = models.BooleanField(
        default=False
    )
    holistic_alternative_treatment_factor = models.BooleanField(
        default=False
    )
    boarding_advertising_holoday_cancellation_rate = models.BooleanField(
        default=False
    )
    breeding_endorsement = models.CharField(
        blank=True,
        max_length=255,
        choices=BREEDING_ENDORSEMENT_LIST
    )
    discount_factor = models.CharField(
        blank=True,
        max_length=255,
    )
    digital_partner_factor = models.BooleanField(
        default=False
    )
    affinity_group_factor = models.BooleanField(
        default=False
    )
    smart_collar_factor = models.BooleanField(
        default=False
    )
    employee_benefit_factor = models.DecimalField(
        default=0,
        max_digits=4,
        decimal_places=2
    )
    default = models.BooleanField(
        null=True,
        help_text=_(
            'Both "Unknown" and "No" means that the plan is not default'
        ),
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
    premium_cost = models.DecimalField(
        default=50,
        max_digits=4,
        decimal_places=2
    )
    created = models.DateTimeField(_('created'), db_index=True)
    recurrence = models.CharField(
        blank=True,
        max_length=255,
        choices=RECURRENCE_LIST,
        default=RECURRENCE_LIST.Yearly
    )

    def __str__(self):
        return self.quote_id


class PaymentListMonth(models.Model):
    """List of payments dates for monthly payment option"""
    paymentList_id = models.CharField(
        max_length=255,
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        blank=False,
        null=False,
    )
    myList = models.TextField(null=True, default=payment_list)

    quote_number = models.OneToOneField(
        'Quote',
        default=None,
        verbose_name=_('quote'),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.paymentList_id


class Policy(models.Model):
    """Currently selected plan for user account"""
    policy_id = models.CharField(
        max_length=255,
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.CASCADE
    )
    # quote_number = models.ForeignKey(
    #     'Quote',
    #     verbose_name=_('quote'),
    #     on_delete=models.CASCADE
    # )
    paymentListMonth_number = models.OneToOneField(
        'PaymentListMonth',
        verbose_name=_('payment list Month'),
        on_delete=models.CASCADE
    )
    expire = models.DateField(
        _('expire'), default=next_year, blank=True, null=True, db_index=True)
    active = models.BooleanField(_('active'), default=False, db_index=True)

    def __str__(self):
        return self.policy_id

    def make_monthly_payment(self):
        """Check whetre there is a need to charge the user"""
        current_date = datetime.date.today()
        next_payment = self.paymentListMonth_number.myList[0]

        if current_date == next_payment:
            """make a payment"""
            return self.paymentListMonth_number.myList[0]
        else:
            return None
