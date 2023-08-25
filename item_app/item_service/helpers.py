import uuid
from rest_framework.response import Response


class ResponseHelper():
    def __init__(self, status, message, data=None):
        self.status = status
        self.message = message
        self.data = data

    def helper_response(self):
        return Response({
            'status': self.status,
            'message': self.message,
            'data': self.data
        })

    def helper_response_without_data(self):
        return Response({
            'status': self.status,
            'message': self.message,
        })


class GetObjectHelper():
    def __init__(self, model, id):
        self.model = model
        self.id = id

    def get_object(self):
        '''
        Helper method to get the object with the given uuid
        '''
        try:
            uuid.UUID(self.id)
        except Exception:
            return None

        try:
            return self.model.objects.get(uuid=self.id)
        except:
            return None


class BodyHelper():
    def __init__(self, data):
        self.data = data

    def parser_data(self):
        '''
        method helper to parse data from request body
        to be used in create_item method in views.py
        '''

        name = self.data['name']
        type = self.data['type']
        prices = self.data['prices']

        regular_price = None
        vip_price = None
        wholesale_price = None

        for p in prices:
            if p['priceFor'] == 'regular':
                regular_price = p['price']
            elif p['priceFor'] == 'vip':
                vip_price = p['price']
            elif p['priceFor'] == 'wholesale':
                wholesale_price = p['price']
            else:
                print('error')

        try:
            if vip_price is None:
                vip_price = regular_price
        except:
            pass

        try:
            if wholesale_price is None:
                wholesale_price = regular_price
        except:
            pass

        return {
            'name': name,
            'type': type,
            'regular_price': regular_price,
            'vip_price': vip_price,
            'wholesale_price': wholesale_price
        }
