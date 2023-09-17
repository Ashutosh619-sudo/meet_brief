from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import CustomUser


class UserCreate(APIView):

    def post(self, request):
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomTokenObtainPairView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)


        if email is None or password is None:
            return Response({'detail': 'Both email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

            # Attempt to authenticate the user using the provided email and password
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'detail':"The User Doesn't exists, please log in first"})
        
        if user:
            # If authentication is successful, generate and return the token
            token = Token.objects.get(user=user)
            return Response({"token":token.key})
        else:
            return Response({'detail': 'Unable to log in with provided credentials.'}, status=status.HTTP_401_UNAUTHORIZED)