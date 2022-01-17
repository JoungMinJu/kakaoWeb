
from django.urls import path, include
from .views import *

app_name = 'user'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]
