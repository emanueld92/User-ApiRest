from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from .serializers import UserSerializers

# Create your views here.

class UserAPi(APIView):
    def post(self, request):
        serializers= UserSerializers(data= request.data)
        if serializers.is_valid():
            user= serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)
        