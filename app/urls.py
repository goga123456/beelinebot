from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from app.bot import BotAPIView

urlpatterns = [
    path('bot', csrf_exempt(BotAPIView.as_view()))
]
