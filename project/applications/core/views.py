from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import RegistrationSerializer, LoginSerializer
from core.swagger import registration_schema, login_schema


class RegistrationAPIView(APIView):

    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    @swagger_auto_schema(
        request_body=registration_schema,
        responses={
            '201': '{"Token: 5279c3f8e1d1257b1d8c6391c30937614161abad"}',
            '400': "Invalid data",
        },
        operation_id='Регистрация',
        operation_description='Регистрация юзера.\n Возвращает authtoken или ошибку',
    )
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=login_schema,
        responses={
            '200': '{"Token: 5279c3f8e1d1257b1d8c6391c30937614161abad"}',
            '400': "Invalid data",
        },
        operation_id='Вход',
        operation_description='Вход юзера.\n Возвращает authtoken или ошибку',
    )
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK,
        )
