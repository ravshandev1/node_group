from django.urls import path
from .views import MessageView, chat

urlpatterns = [
    path('message/', chat, name='message'),
]
