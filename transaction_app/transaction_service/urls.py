# from django.conf.urls import url # linux
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_transaction, name='create transaction'),
]