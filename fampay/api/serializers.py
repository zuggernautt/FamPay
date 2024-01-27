from .models import Video, APIAuthKey
from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        

class APIAuthKeySerializer(serializers.ModelSerializer):
    """
        Class for APIAuthKey Model Serialization
    """
    class Meta:
        model = APIAuthKey
        fields = '__all__'