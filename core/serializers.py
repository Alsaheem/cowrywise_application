from .models import MyUUIDCreator
from rest_framework import serializers


class MyUUIDCreatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUUIDCreator
        fields = ["generated_id", "created_at", "updated_at"]
