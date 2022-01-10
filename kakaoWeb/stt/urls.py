
from django.urls import path, include
from .views import *

app_name = 'stt'
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('chat', chat, name='chat'),
    path('chat_two',chat_two, name='chat_two'),
    path('error', error, name='error'),
]
