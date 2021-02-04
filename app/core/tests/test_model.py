from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

import datetime


def sample_user(email='test@rainwalk.io', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


def sample_quote():
    """Create a sample quote"""
    return models.Quote.objects.create(
        quote_id='2c4b9151-7795-4eca-b45c-015bdd2d9c50',
        created=datetime.date.today(),
    )


def sample_paymentlistmonth():
    """Create a sample payment month list"""
    return models.PaymentListMonth.objects.create(
        paymentList_id='3c4b915e-7795-4ec1-b45c-015bdd2d9c50'
    )


class ModelTest(TestCase):

    def test_create_user_with_email_successfult(self):
        """Test creating a new user with an email is successful"""
        email = 'test@rainwalk.io'
        password = 'Password12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@RAINWALK.io'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                'Test1234'
            )

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@rainwalk.io',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_quote_str(self):
        """Test the quote string representation"""
        quote = models.Quote.objects.create(
            quote_id='2c4b915e-7795-4eca-b45c-015bdd2d9c50',
            pet_name='MAXX',
            base_rate=54.11,
            geographical_factor='1.066',
            created=datetime.date.today(),
        )

        self.assertEqual(str(quote), quote.quote_id)

    def test_paymentlistmonth_str(self):
        """Test the payment list month sting representation"""
        paymentlistmonth = models.PaymentListMonth.objects.create(
            paymentList_id='3c4b915e-7795-4eca-b45c-015bdd2d9c50'
        )

        self.assertEqual(
            str(paymentlistmonth),
            paymentlistmonth.paymentList_id
        )

    def test_policy_str(self):
        """Test the policy string representation"""
        policy = models.Policy.objects.create(
            policy_id='4c4b915e-7795-4eca-b45c-015bdd2d9c50',
            user=sample_user(),
            policy_quote_number=sample_quote(),
            policy_paymentListMonth_number=sample_paymentlistmonth()
        )

        self.assertEqual(
            str(policy),
            policy.policy_id
        )
