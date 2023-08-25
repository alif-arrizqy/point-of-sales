# from django.conf.urls import url # linux
from django.urls import path, include
from . import views

urlpatterns = [
    # path('user/', UserListView.as_view()),
    # path('user/<user_id>/', views.UserDetailView.as_view()),
    path('', views.list_users, name='get user'),
    path('create/', views.create_user, name='create user'),
    path('<uuid>/', views.get_user, name='get user by uuid'),
    path('update/<uuid>/', views.update_user, name='update user'),
    path('delete/<uuid>/', views.delete_user, name='delete user'),
]