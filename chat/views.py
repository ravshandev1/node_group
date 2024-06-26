from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from django.shortcuts import render


def chat(req):
    return render(req, 'chat.html')


class MessageView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = serializer.validated_data['message']
        return Response({'message': 'Message received'}, status=status.HTTP_201_CREATED)
