import uuid
from rest_framework.response import Response


class ResponseHelper():
    def __init__(self, status, message, data=None):
        self.status = status
        self.message = message
        self.data = data

    def helper_response(self):
        return Response({
            'status_code': self.status,
            'message': self.message,
            'data': self.data
        })

    def helper_response_without_data(self):
        return Response({
            'status_code': self.status,
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