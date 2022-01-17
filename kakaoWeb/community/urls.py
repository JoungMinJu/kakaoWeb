
from django.urls import path, include
from .views import *

app_name = 'community'
urlpatterns = [
    path('', show, name="show"),
    path('<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    path('<str:community_id>/create_comment', create_comment, name="create_comment"),
    path('<int:comment_id>/update_comment', update_comment, name="update_comment"),
    path('<int:comment_id>/delete_comment', delete_comment, name="delete_comment"),
    path('<int:community_id>/community_like', community_like, name="community_like"),
]
