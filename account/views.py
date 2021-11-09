from rest_framework import viewsets
from rest_framework.response import Response


class TestView(viewsets.ViewSet):
    def list(self, request):
        data = {
            "name": "sajjad",
            "last": "ahmad"
        }
        return Response(data)
