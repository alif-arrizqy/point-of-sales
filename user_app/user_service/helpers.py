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
