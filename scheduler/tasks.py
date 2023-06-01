from celery import shared_task
from .modules import email_check


@shared_task
def print_hello():
    print("hello mason")
    return "test"


@shared_task
def daily_test():
    return "mason test"


@shared_task
def slack_bot():
    email_cs = email_check.EmailCSIssueCheck()
    email_cs.minute_check()
