
from django.urls import path, include
from .views import *

app_name = 'stt'
urlpatterns = [
    path('', intro, name='intro'),
    path('mainpage', mainpage,name='mainpage'),
    path('chat', chat, name='chat'),
    path('chat_two',chat_two, name='chat_two'),
    path('error', error, name='error'),
    path('error_two', error_two, name = 'error_two'),
    path('gate', gate,name='gate'),
]
