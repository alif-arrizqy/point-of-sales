# from django.conf.urls import url # linux
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_users, name='get user'),
    path('find-name/', views.find_user_name, name='find user by name'),
    path('create/', views.create_user, name='create user'),
    path('<uuid>/', views.get_user, name='get user by uuid'),
    path('update/<uuid>/', views.update_user, name='update user'),
    path('delete/<uuid>/', views.delete_user, name='delete user'),
]