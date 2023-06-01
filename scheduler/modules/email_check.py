import requests
import logging
from django.conf import settings

logger = logging.getLogger("factor_async_log")


class EmailCSIssueCheck:
    def minute_check(self):
        req = requests.post(
            settings.SLACK_WEB_HOOK_URL,
            json={"text": ":p"}
        )
        logger.info(req.status_code)
