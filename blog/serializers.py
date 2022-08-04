# from django.contrib.auth.models import *
from rest_framework import serializers
from . import models

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields="__all__"
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields="__all__"
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Entry
        fields="__all__"


# class CatagorySerializer(serializers.Serializer):
#     name=serializers.CharField(required=False, allow_blank=True, max_length=100)
