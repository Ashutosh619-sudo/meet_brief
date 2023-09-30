from rest_framework import serializers
from .models import Meeting, Caption


class FileUploadSerializer(serializers.Serializer):

    file = serializers.FileField()


class CaptionSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Caption
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):

    caption = CaptionSerializer(read_only=True, required=False)

    class Meta:
        model = Meeting
        fields = '__all__'