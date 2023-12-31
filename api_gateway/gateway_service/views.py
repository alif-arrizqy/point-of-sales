import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from .settings import HOST_USER, HOST_ITEM, HOST_TRANSACTION


# user service
@swagger_auto_schema(method='GET')
@api_view(['GET'])
def get_users(self):
    '''
    Get all users from user service
    '''
    try:
        url = f'{HOST_USER}/'
        response = requests.get(url)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )


@swagger_auto_schema(method='GET', description='Get user by uuid')
@api_view(['GET'])
def get_user_by_uuid(self, uuid):
    '''
    Get user by uuid
    '''
    try:
        url = f'{HOST_USER}/{uuid}/'
        response = requests.get(url)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )


@swagger_auto_schema(method='POST', request_body=UserBodySwagger)
@api_view(['POST'])
def create_user(request):
    '''
    Create a new post
    '''
    try:
        url = f'{HOST_USER}/create/'
        response = requests.post(url, json=request.data)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )

@swagger_auto_schema(method='POST', request_body=FindUserSwagger, description='Find user by name')
@api_view(['POST'])
def find_user(request):
    '''
    Find user by name
    '''
    try:
        url = f'{HOST_USER}/find-name/'
        response = requests.post(url, json=request.data)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )

@swagger_auto_schema(method='PUT', request_body=UserBodySwagger)
@api_view(['PUT'])
def update_user(request, uuid):
    '''
    Update a user by uuid
    '''
    try:
        url = f'{HOST_USER}/update/{uuid}/'
        response = requests.put(url, json=request.data)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )

@swagger_auto_schema(method='DELETE')
@api_view(['DELETE'])
def delete_user(request, uuid):
    '''
    Delete a user by uuid
    '''
    try:
        url = f'{HOST_USER}/delete/{uuid}/'
        response = requests.delete(url)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )

# item service
@swagger_auto_schema(method='GET')
@api_view(['GET'])
def get_items(self):
    '''
    Get all items from item service
    '''
    try:
        url = f'{HOST_ITEM}/'
        response = requests.get(url)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )


@swagger_auto_schema(method='GET', description='Get item by uuid')
@api_view(['GET'])
def get_item_by_uuid(self, uuid):
    '''
    Get item by uuid
    '''
    try:
        url = f'{HOST_ITEM}/{uuid}/'
        response = requests.get(url)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )


@swagger_auto_schema(method='POST', request_body=ItemBodySwagger)
@api_view(['POST'])
def create_item(request):
    '''
    Create a new post
    '''
    try:
        url = f'{HOST_ITEM}/create/'
        response = requests.post(url, json=request.data)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )

@swagger_auto_schema(method='POST', request_body=FindItemSwagger, description='Find item by name')
@api_view(['POST'])
def find_item(request):
    '''
    Find item by name
    '''
    try:
        url = f'{HOST_ITEM}/find-name/'
        response = requests.post(url, json=request.data)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )

@swagger_auto_schema(method='PUT', request_body=ItemBodySwagger)
@api_view(['PUT'])
def update_item(request, uuid):
    '''
    Update a item by uuid
    '''
    try:
        url = f'{HOST_ITEM}/update/{uuid}/'
        response = requests.put(url, json=request.data)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )

@swagger_auto_schema(method='DELETE')
@api_view(['DELETE'])
def delete_item(request, uuid):
    '''
    Delete a item by uuid
    '''
    try:
        url = f'{HOST_ITEM}/delete/{uuid}/'
        response = requests.delete(url)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )

# transaction service
@swagger_auto_schema(method='POST', request_body=TransactionBodySwagger)
@api_view(['POST'])
def create_transaction(request):
    '''
    Create a new transaction
    '''
    try:
        url = f'{HOST_TRANSACTION}/create/'
        response = requests.post(url, json=request.data)
        return Response(response.json())
    except Exception:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='internal server error'
        )