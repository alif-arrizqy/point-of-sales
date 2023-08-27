from django.urls import path, include
from . import views

user_service_patterns = [
    path('', views.get_users, name='user service'),
    path('find-name/', views.find_user, name='user service'),
    path('create/', views.create_user, name='user service'),
    path('<uuid>/', views.get_user_by_uuid, name='user service'),
    path('update/<uuid>/', views.update_user, name='user service'),
    path('delete/<uuid>/', views.delete_user, name='user service'),
]

urlpatterns = [
    path('user/', include(user_service_patterns))
]