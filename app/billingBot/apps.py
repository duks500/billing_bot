from django.apps import AppConfig
import os


class BillingbotConfig(AppConfig):
    name = 'billingBot'

    # def ready(self):
    #     from . import jobs
    #
    #     if os.environ.get('RUN_MAIN', None) != 'true':
    #         jobs.start_scheduler(
