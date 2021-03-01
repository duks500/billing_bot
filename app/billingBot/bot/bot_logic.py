from core.models import User, PaymentListMonth, Policy

import datetime
from dateutil.relativedelta import relativedelta


def payment_list_month():
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


def payment_list_year():
    """A list with all the difrrent dates"""
    startDate = datetime.date.today()
    # startDate = startDate+relativedelta(day=+31)
    PAYMENT_LIST = [
        f'{startDate+relativedelta(months=+0)}'
        ]
    return PAYMENT_LIST


def monthly_or_yearly_bot(pk):
    """
        A function that checks what plan the user has chosen(yearly/monthly)
        and create a new list in the database
    """
    policy = Policy.objects.get(pk=pk)
    policy_recurrence = policy.paymentListMonth_number.quote_number.recurrence
    print(policy_recurrence)

    if policy_recurrence == 'Monthly':
        print(policy_recurrence)
        policy.paymentListMonth_number.myList = payment_list_month()
        policy.save()
        print(policy.paymentListMonth_number.myList)

    elif policy_recurrence == 'Yearly':
        print(policy_recurrence)
        policy.paymentListMonth_number.myList = payment_list_year()
        policy.save()
        print(policy.paymentListMonth_number.myList)

    return policy


def no_pay_bot():
    """
        A function that deal with a payament error(from the client side)
    """
    pass