import email

import requests
import imaplib
import logging
from django.conf import settings
from rest_framework import views, permissions, status, response
from email.header import decode_header

logger = logging.getLogger("factor_async_log")


class SlackAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        # Test
        # import pymysql
        #
        # conn = pymysql.connect(host="localhost", user="tsh_gip", password="admin", db="gip_mysql", charset="utf8")
        #
        # curs = conn.cursor()
        #
        # sql = "select * from authentication_number;"
        # curs.execute(sql)
        #
        # rows = curs.fetchall()
        # logger.info(rows)
        #
        # conn.close()

        # 확인할 메일 계정
        # user = "factorlabs"
        # password = "Gipmxbc1@#"
        #
        # # 메일 접속
        # imap = imaplib.IMAP4_SSL("imap.daum.net")
        # imap.login(user, password)
        # imap.select("inbox")
        #
        # # imap_status, message = imap.uid("search", None, '(FROM "conficker77@gmail.com")')
        # imap_status, message = imap.uid("search", None, "ALL")
        # message = message[0].split()
        #
        # for n, message in enumerate(message):
        #     logger.info(f"writing email #{n} on file")
        #     res, msg = imap.uid("fetch", message, "(RFC822)")
        #     raw = msg[0][1]
        #     email_message = email.message_from_bytes(raw)
        #     # email_message = email.message_from_string(raw.decode("utf-8"))
        #
        #     # logger.info(email_message["From"])
        #
        #     subject, encoding = decode_header(email_message['Subject'])[0]
        #     logger.info(subject)
        #
        # imap.close()
        # imap.logout()

        # slack
        # requests.post(
        #     settings.SLACK_WEB_HOOK_URL,
        #     json={"text": "test"}
        # )
        return response.Response(data={"asd": True}, status=status.HTTP_200_OK)
