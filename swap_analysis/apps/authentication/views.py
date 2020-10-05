from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework import status
from django.contrib.auth import authenticate
from swap_analysis.apps.authentication.serializers import LoginSerializer
from swap_analysis.apps.authentication.models import User


class CustomAuthToken(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = User.objects.filter(
            email=email).first()

        if not user:
            raise AuthValidationExcpetion()

        user_auth = authenticate(username=email, password=password)

        if not user_auth:
            raise AuthValidationExcpetion()

        token, created = Token.objects.get_or_create(user=user_auth)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class AuthValidationExcpetion(exceptions.APIException):
    """Exception to raise if the data validation fails"""
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self):
        self.detail = "Invalid email or password"
