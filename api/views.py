from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TaskSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import permissions
from user.models import User
from task.models import Task

class TaskView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            print(serializer.validated_data)
            owner = request.user
            serializer.save(owner=owner)
            return Response({"Success": serializer.data}, status=201)
        return Response({"Failure": serializer.errors}, status=400)

    def get(self, request, *args, **kwargs):
        if kwargs.get("id"):
            instance = Task.objects.get(id=kwargs.get("id"), owner=request.user)
            if instance:
                serializer = TaskSerializer(instance=instance)
                if serializer.is_valid():
                    data = serializer.data
                    return Response({"data": data}, status=200)
                return Response({"error": serializer.errors}, status=400)
            else:
                return Response({"error": "Item not Found"}, status=404)
        else:
            tasks = Task.objects.filter(owner=request.user)
            serializer = TaskSerializer(instance=tasks, many=True)
            print(tasks)
            if tasks:
                data = serializer.data
                return Response({"data": data}, status=200)
#                return Response({"error": serializer.errors}, status=402)
            else:
                return Response({"error": "Items not Found"}, status=404)

    def patch(self, request, *args, **kwargs):
        data = request.data
        id = kwargs.get("id")
        owner = request.user
        instance = Task.objects.get(id=id, owner=owner)
        if instance:
            serializer = TaskSerializer(instance=instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                return Response({"Success": data}, status=200)
            return Response({"error": serializer.errors}, status=400)
        else:
            return Response({"error": "Item not Found"}, status=404)

    def put(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        id = kwargs.get("id")
        instance = Task.objects.get(owner=user, id=id)
        if instance:
            serializer = TaskSerializer(instance=instance, data=data)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                return Response({"Success": data}, status=200)
            return Response({"error": serializer.errors}, status=402)
        else:
            return Response({"error": "Item not Found"}, status=404)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        owner = self.request.user
        instance = Task.objects.get(id=id, owner=owner)
        if instance:
            instance.delete()
            return Response({"Success": "Successfully deleted"}, status=204)
        else:
            return Response({"error": "Object not found"}, status=404)


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
        return Response({"User": serializer.data}, status=200)

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": serializer.data}, status=200)
        return Response({"Failed to Patch": serializer.errors}, status=400)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": serializer.data}, status=201)
        return Response({"Failure": serializer.errors}, status=400t)
