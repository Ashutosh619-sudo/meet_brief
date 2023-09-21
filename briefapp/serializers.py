from rest_framework import serializers
from .models import Meeting, Caption


class FileUploadSerializer(serializers.Serializer):

    file = serializers.FileField()


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = ['id', 'title', 'start_time', 'end_time','creator']

class CaptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caption
        fields = '__all__'