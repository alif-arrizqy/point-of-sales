from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import User
from .serializers import UserSerializer


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            'name': request.data.get('name'),
            'type': request.data.get('type')
        }

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_201_CREATED,
                'message': 'create user is success',
                'data': serializer.data
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'create user is failed',
            'data': serializer.errors
        })


class UserDetailView(APIView):
    def get_object(self, user_id):
        print(user_id)

        try:
            return User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'user not found',
                'data': None
            })
    
    def get(self, request, user_id):
        print(user_id)
        user = self.get_object(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)