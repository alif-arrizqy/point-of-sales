import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer
from .helpers import ResponseHelper, BodyHelper, GetObjectHelper
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='GET', responses={200: ItemSerializer(many=True)})
@api_view(['GET'])
def list_items(request):
    '''
    Get all items
    '''
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return ResponseHelper(
            status=status.HTTP_200_OK,
            message='get all items is success',
            data=serializer.data
        ).helper_response()
    else:
        return ResponseHelper(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            message='method not allowed'
        ).helper_response_without_data()


@swagger_auto_schema(method='POST', request_body=ItemSerializer)
@api_view(['POST'])
def create_item(request):
    '''
    Create a new item
    '''
    if request.method == 'POST':
        # parse data
        body = BodyHelper(data=request.data)
        serializer = ItemSerializer(data=body.parser_data())
        if serializer.is_valid():
            serializer.save()
            return ResponseHelper(
                status=status.HTTP_201_CREATED,
                message='create item is success',
                data=serializer.data
            ).helper_response()
        else:
            return ResponseHelper(
                status=status.HTTP_400_BAD_REQUEST,
                message='create item is failed',
                data=serializer.errors
            ).helper_response()
    else:
        return ResponseHelper(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            message='method not allowed'
        ).helper_response_without_data()


@swagger_auto_schema(method='GET', responses={200: ItemSerializer})
@api_view(['GET'])
def get_item(request, uuid):
    '''
    retrieve a item by uuid
    '''
    item = GetObjectHelper(model=Item, id=uuid).get_object()
    if not item:
        return ResponseHelper(
            status=status.HTTP_404_NOT_FOUND,
            message='item not found'
        ).helper_response_without_data()

    serializer = ItemSerializer(item)
    return ResponseHelper(
        status=status.HTTP_200_OK,
        message='get item is success',
        data=serializer.data
    ).helper_response()


@swagger_auto_schema(method='PUT', request_body=ItemSerializer)
@api_view(['PUT'])
def update_item(request, uuid):
    '''
    update a item by uuid
    '''
    item = GetObjectHelper(model=Item, id=uuid).get_object()
    if not item:
        return ResponseHelper(
            status=status.HTTP_404_NOT_FOUND,
            message='item not found'
        ).helper_response_without_data()

    # parse data
    body = BodyHelper(data=request.data)
    serializer = ItemSerializer(item, data=body.parser_data())
    if serializer.is_valid():
        serializer.save()
        return ResponseHelper(
            status=status.HTTP_200_OK,
            message='update item is success',
            data=serializer.data
        ).helper_response()
    else:
        return ResponseHelper(
            status=status.HTTP_400_BAD_REQUEST,
            message='update item is failed',
            data=serializer.errors
        ).helper_response()


@swagger_auto_schema(method='DELETE')
@api_view(['DELETE'])
def delete_item(request, uuid):
    '''
    delete a item by uuid
    '''
    item = GetObjectHelper(model=Item, id=uuid).get_object()
    if not item:
        return ResponseHelper(
            status=status.HTTP_404_NOT_FOUND,
            message='item not found'
        ).helper_response_without_data()

    item.delete()
    return ResponseHelper(
        status=status.HTTP_200_OK,
        message='delete item is success'
    ).helper_response_without_data()
