from django.urls import path
from .views import *

urlpatterns = [
        path('api/', FriendView.as_view()),
        path('api/<int:pk>', FriendDetailView.as_view()),
]