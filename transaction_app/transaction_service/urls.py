# from django.conf.urls import url # linux
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.list_items, name='list all items'),
    path('create/', views.create_transaction, name='create transaction'),
    # path('<uuid>/', views.get_item, name='get item by uuid'),
    # path('update/<uuid>/', views.update_item, name='update item'),
    # path('delete/<uuid>/', views.delete_item, name='delete item'),
]