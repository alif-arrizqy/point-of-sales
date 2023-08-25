from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from .helpers import ResponseHelper, GetObjectHelper
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='GET', responses={200: UserSerializer(many=True)})
@api_view(['GET'])
def list_users(request):
    '''
    Get all users
    '''
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return ResponseHelper(
            status=status.HTTP_200_OK,
            message='get all users is success',
            data=serializer.data
        ).helper_response()
    else:
        return ResponseHelper(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            message='method not allowed'
        ).helper_response_without_data()


@swagger_auto_schema(method='POST', request_body=UserSerializer)
@api_view(['POST'])
def create_user(request):
    '''
    Create a new user
    '''
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseHelper(
                status=status.HTTP_201_CREATED,
                message='create user is success',
                data=serializer.data
            ).helper_response()

        return ResponseHelper(
            status=status.HTTP_400_BAD_REQUEST,
            message='create user is failed',
            data=serializer.errors
        ).helper_response()
    else:
        return ResponseHelper(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            message='method not allowed'
        ).helper_response_without_data()


@swagger_auto_schema(method='GET', responses={200: UserSerializer})
@api_view(['GET'])
def get_user(request, uuid):
    '''
    retrieve a user by uuid
    '''
    user = GetObjectHelper(model=User, id=uuid).get_object()
    if not user:
        return ResponseHelper(
            status=status.HTTP_404_NOT_FOUND,
            message='user not found'
        ).helper_response_without_data()

    serializer = UserSerializer(user)
    return ResponseHelper(
        status=status.HTTP_200_OK,
        message='get user is success',
        data=serializer.data
    ).helper_response()


@swagger_auto_schema(method='GET', responses={200: UserSerializer})
@api_view(['GET'])
def find_user_name(request):
    '''
    retrieve a user by name
    '''
    name = request.data.get('name')
    if not name:
        return ResponseHelper(
            status=status.HTTP_400_BAD_REQUEST,
            message='name is required'
        ).helper_response_without_data()

    users = User.objects.filter(name__icontains=name)
    if not users:
        return ResponseHelper(
            status=status.HTTP_404_NOT_FOUND,
            message='user not found'
        ).helper_response_without_data()

    serializer = UserSerializer(users, many=True)
    return ResponseHelper(
        status=status.HTTP_200_OK,
        message='get user is success',
        data=serializer.data
    ).helper_response()


@swagger_auto_schema(method='PUT', request_body=UserSerializer)
@api_view(['PUT'])
def update_user(request, uuid):
    '''
    Update a user by uuid if exist
    '''
    if request.method == 'PUT':
        user = GetObjectHelper(model=User, id=uuid).get_object()
        if not user:
            return ResponseHelper(
                status=status.HTTP_404_NOT_FOUND,
                message='user not found'
            ).helper_response_without_data()

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseHelper(
                status=status.HTTP_200_OK,
                message='update user is success',
                data=serializer.data
            ).helper_response()

        return ResponseHelper(
            status=status.HTTP_400_BAD_REQUEST,
            message='update user is failed',
            data=serializer.errors
        ).helper_response()
    else:
        return ResponseHelper(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            message='method not allowed'
        ).helper_response_without_data()


@swagger_auto_schema(method='DELETE')
@api_view(['DELETE'])
def delete_user(request, uuid):
    '''
    Delete a user by uuid if exist
    '''
    user = GetObjectHelper(model=User, id=uuid).get_object()
    if not user:
        return ResponseHelper(
            status=status.HTTP_404_NOT_FOUND,
            message='user not found'
        ).helper_response_without_data()

    user.delete()
    return ResponseHelper(
        status=status.HTTP_200_OK,
        message='delete user is success',
    ).helper_response_without_data()
