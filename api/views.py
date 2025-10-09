from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TaskSerializer, UserSerializer
from rest_framework.response import Response 
from rest_framework import permissions

class TaskView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            print(serializer.data)
            owner = request.user
            serializer.save(owner=owner)
            return Response({"Success":serializer.data}, status=200)
        return Response({"Failure":serializer.errors}, status=400)


class UserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success":serializer.data}, status=200)
        return Response({"Failure":serializer.errors}, status=400)

