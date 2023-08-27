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

item_service_patterns = [
    path('', views.get_items, name='item service'),
    path('find-name/', views.find_item, name='item service'),
    path('create/', views.create_item, name='item service'),
    path('<uuid>/', views.get_item_by_uuid, name='item service'),
    path('update/<uuid>/', views.update_item, name='item service'),
    path('delete/<uuid>/', views.delete_item, name='item service'),
]

transaction_service_patterns = [
    path('create/', views.create_transaction, name='transaction service'),
]

urlpatterns = [
    path('user/', include(user_service_patterns)),
    path('item/', include(item_service_patterns)),
    path('transaction/', include(transaction_service_patterns)),
]