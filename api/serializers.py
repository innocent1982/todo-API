from rest_framework import serializers
from user.models import User
from task.models import Task
from .utility_serializers import DefaultUser

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=User
        fields = "__all__"

    def update(self, instance, validated_data):
        print(validated_data)
        return super().update(instance, validated_data)

class TaskSerializer(serializers.ModelSerializer):
    owner = DefaultUser(read_only=True)
    class Meta:
        model=Task
        fields = [
           "duration", "owner", "name", "description", "priority", "start_time", "end_time"
        ]
        extra_kwargs = {
            "duration":{ "read_only": True }
        }



