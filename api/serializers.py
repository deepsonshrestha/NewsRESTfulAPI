from rest_framework import serializers
from django.contrib.auth.models import User

from .models import NewsModel

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewsModel
        fields='__all__'


