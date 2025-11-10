from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import (
    UserSerializer,
    UserRegistrationSerializer,
    EmailAuthTokenSerializer,
    AuthResponseSerializer,
)

User = get_user_model()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        tags=['Authentication'],
        request=UserRegistrationSerializer,
        responses={
            status.HTTP_201_CREATED: AuthResponseSerializer,
        },
        summary="Register a new user",
        description="Create a new user account and receive JWT tokens (access and refresh).",
    )
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = get_tokens_for_user(user)
        return Response(
            {
                "user": UserSerializer(user).data,
                "access": tokens['access'],
                "refresh": tokens['refresh'],
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        tags=['Authentication'],
        request=EmailAuthTokenSerializer,
        responses={
            status.HTTP_200_OK: AuthResponseSerializer,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Invalid credentials"),
        },
        summary="Obtain JWT tokens",
        description="Authenticate using email and password to receive JWT tokens (access and refresh).",
    )
    def post(self, request, *args, **kwargs):
        serializer = EmailAuthTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        tokens = get_tokens_for_user(user)
        return Response(
            {
                "user": UserSerializer(user).data,
                "access": tokens['access'],
                "refresh": tokens['refresh'],
            },
            status=status.HTTP_200_OK,
        )


class RefreshTokenView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        tags=['Authentication'],
        request={'type': 'object', 'properties': {'refresh': {'type': 'string'}}},
        responses={
            status.HTTP_200_OK: {'type': 'object', 'properties': {'access': {'type': 'string'}}},
        },
        summary="Refresh access token",
        description="Get a new access token using a refresh token.",
    )
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response(
                {'error': 'Refresh token is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            token = RefreshToken(refresh_token)
            return Response({
                'access': str(token.access_token),
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': 'Invalid or expired refresh token'},
                status=status.HTTP_400_BAD_REQUEST
            )


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        tags=['Authentication'],
        request={'type': 'object', 'properties': {'refresh': {'type': 'string'}}},
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(description="Successfully logged out"),
        },
        summary="Log out",
        description="Blacklist the current refresh token.",
    )
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
        except Exception:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

