from rest_framework import serializers
from user.models import User
from task.models import Task

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=User
        fields = "__all__"

class TaskManager(serializers.ModelSerializer):
    owner = DefaultUser(read_only=True)
    class Meta:
        model=Task
        fields = [
           "duration", "owner", "name", "description", "priority", "start_date", "end_date"
        ]
        extra_kwargs = {
            "duration":{ "read_only": True }
        }


class DefaultUser(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username= serializers.CharField(read_only=True)
