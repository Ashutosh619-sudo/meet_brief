from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .serializers import FileUploadSerializer, CaptionSerializer
import boto3
import os
import json

from .models import Meeting, Caption
from .serializers import MeetingSerializer

from .permissions import IsObjectCreator

class Caption(generics.CreateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]


    def _setup_boto(self):

        aws_key = os.environ['AWS_ACCESS_KEY']
        aws_secret = os.environ['AWS_SECRET_KEY']

        session = boto3.Session(aws_access_key_id=aws_key,aws_secret_access_key=aws_secret)
        s3 = session.client('s3')
        return s3

    def post(self, request):

        caption_data = {}
        file_name = request.data["file_name"]
        conversation = request.data["conversation"]
        caption_data["meeting"] = request.data["meeting"]
        file_name = "{}.json".format(file_name)

        s3 = self._setup_boto()
        
        bucket_name = os.environ["AWS_BUCKET"]
        path = str(request.user.id)

        object_key  = path + '/' + file_name

        uploading_data = {
            "conversation":conversation
        }

        json_data = json.dumps(uploading_data)

        try:
            s3.put_object(Bucket=bucket_name, Key=object_key, Body=json_data)
            caption_data['object_key'] = object_key
            caption_data['file_name'] = file_name

            serializer = CaptionSerializer(data=caption_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

            return Response({'detail': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'detail': 'Failed to upload the file to S3.', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MeetingsListCreate(generics.ListCreateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    serializer_class = MeetingSerializer

    def get_queryset(self):
        user = self.request.user
        return Meeting.objects.filter(creator=user)

class MeetingsRetreiveUpdate(generics.RetrieveUpdateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, IsObjectCreator]

    serializer_class = MeetingSerializer

    queryset = Meeting.objects.all()

