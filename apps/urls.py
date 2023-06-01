from django.urls import path, include
from . import views as rest_view

app_name = "v1_apps"

urlpatterns = [
    path("slack-test", rest_view.SlackAPIView.as_view(), name="v1_slack")
]
