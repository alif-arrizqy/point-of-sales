import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from .models import Transaction
from .serializers import TransactionSerializer, TransactionBodySwagger
from .helpers import *
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='POST', request_body=TransactionBodySwagger)
@api_view(['POST'])
def create_transaction(request):
    '''
    Create a new transaction
    '''
    if request.method == 'POST':
        # validation 
        items = ValidationItemHelper(data=request.data)
        if items.item_validation() == False:
            return ResponseHelper(
                status=status.HTTP_404_NOT_FOUND,
                message='item not found, please check item name'
            ).helper_response_without_data()
        
        buyers = ValidationBuyerHelper(data=request.data)
        if buyers.buyer_validation() == False:
            return ResponseHelper(
                status=status.HTTP_404_NOT_FOUND,
                message='buyer not found, please check buyer name'
            ).helper_response_without_data()

        body = BodyTransactionHelper(data=request.data).serialize_data()
        if body:
            resp = BodyTransactionHelper(data=request.data).parser_data()
            return ResponseHelper(
                status=status.HTTP_201_CREATED,
                message='create transaction is success',
                data=resp
            ).helper_response()
        else:
            return ResponseHelper(
                status=status.HTTP_400_BAD_REQUEST,
                message='create transaction is failed',
                data=serializer.errors
            ).helper_response()
    else:
        return ResponseHelper(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            message='method not allowed'
        ).helper_response_without_data()