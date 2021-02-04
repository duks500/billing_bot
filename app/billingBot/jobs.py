from schedule import Scheduler
import threading
import time

from .models import Policy


def check_payment_list():
    policy_lists = Policy.objects.all()
    print(policy_lists)
