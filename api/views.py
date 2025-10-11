from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TaskSerializer, UserSerializer
from rest_framework.response import Response 
from rest_framework import permissions
from user.models import User

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
    def get_permissions(self):
        if self.request.method == "GET" or self.request.method == "PATCH":
            permission_classes = [permissions.IsAuthenticated]
        elif self.request.method == "POST":
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response({"User":serializer.data}, status=200)
    
    def patch(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success":serializer.data}, status=200)
        return Response({"Failed to Patch":serializer.errors}, status=500)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success":serializer.data}, status=200)
        return Response({"Failure":serializer.errors}, status=400)

