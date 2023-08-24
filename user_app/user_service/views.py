import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import User
from .serializers import UserSerializer
from .helpers import ResponseHelper



class UserListView(APIView):
    def get(self, request):
        '''
        Get all users
        '''
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return ResponseHelper(
            status=status.HTTP_200_OK,
            message='get all users is success',
            data=serializer.data
        ).helper_response()

    def post(self, request):
        '''
        Create a new user
        '''
        data = {
            'name': request.data.get('name'),
            'type': request.data.get('type')
        }

        serializer = UserSerializer(data=data)
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


class UserDetailView(APIView):
    def get_object(self, user_id):
        '''
        Helper method to get the object with the given user_id
        '''
        try:
            uuid.UUID(user_id)
        except Exception:
            return None

        try:
            return User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return None

    def get(self, request, user_id):
        '''
        retrieve a user by user_id
        '''
        user = self.get_object(user_id)
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

    def put(self, request, user_id):
        '''
        Update a user by user_id if exist
        '''
        user = self.get_object(user_id)
        if not user:
            return ResponseHelper(
                status=status.HTTP_404_NOT_FOUND,
                message='user not found'
            ).helper_response_without_data()

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'update user is success',
                'data': serializer.data
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'update user is failed',
            'data': serializer.errors
        })

    def delete(self, request, user_id):
        '''
        Delete a user by user_id if exist
        '''
        user = self.get_object(user_id)
        if not user:
            return ResponseHelper(
                status=status.HTTP_404_NOT_FOUND,
                message='user not found'
            ).helper_response_without_data()

        user.delete()
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'delete user is success',
        })
