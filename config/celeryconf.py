from __future__ import absolute_import

import os
from datetime import timedelta

from celery import Celery
from django.conf import settings

from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
app = Celery("conf")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERY_ENABLE_UTC=False,
    CELERYBEAT_SCHEDULE={
        "add-every-2-seconds": {
            "task": "scheduler.tasks.slack_bot",
            "schedule": 500.0,
            # "schedule": 2.0,
            "args": ()
        },
        # "add-scheduler-5-seconds": {
        #     "task": "scheduler.tasks.daily_test",
        #     "schedule": timedelta(seconds=5),
        #     "args": ()
        # }
    },
)
app.conf.timezone = "Asia/Seoul"


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
