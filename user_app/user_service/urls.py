from django.conf.urls import url
from django.urls import path, include
from .views import UserListView, UserDetailView

urlpatterns = [
    path('user/', UserListView.as_view()),
    path('user/<user_id>/', UserDetailView.as_view()),
]