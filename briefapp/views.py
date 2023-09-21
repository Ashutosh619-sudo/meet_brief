from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .serializers import FileUploadSerializer
import boto3
import os

from .models import Meeting
from .serializers import MeetingSerializer

from .permissions import IsObjectCreator

class DownUpCaption(APIView):

    parser_classes = (MultiPartParser,)
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]


    def _setup_boto(self):

        aws_key = os.environ['AWS_ACCESS_KEY']
        aws_secret = os.environ['AWS_SECRET_KEY']

        session = boto3.Session(aws_access_key_id=aws_key,aws_secret_access_key=aws_secret)
        s3 = session.client('s3')
        return s3

    def post(self, request):

        file_serializer = FileUploadSerializer(data=request.data)

        if file_serializer.is_valid():

            uploaded_file = request.FILES['file']

            s3 = self._setup_boto()
            
            bucket_name = os.environ["AWS_BUCKET"]
            path = str(request.user.id)

            object_key  = path + '/' + uploaded_file.name

            try:
                s3.upload_fileobj(uploaded_file, bucket_name, object_key)
                return Response({'detail': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'detail': 'Failed to upload the file to S3.', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeetingsListCreate(generics.ListCreateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    serializer_class = MeetingSerializer

    def get_queryset(self):
        user = self.request.user
        return Meeting.objects.filter(creator=user)

class MeetingsRetreiveUpdate(generics.RetrieveUpdateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    permission_classes = [IsObjectCreator]

    serializer_class = MeetingSerializer

    queryset = Meeting.objects.all()

