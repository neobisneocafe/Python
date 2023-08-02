from random import randint
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from twilio.rest import Client
from config import settings
from .models import User, Cart
from .serializers import LoginSerializer, RegisterSerializer, UserProfileSerializer, UsersListSerializer


@extend_schema(tags=["Register"])
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        phone = request.data.get('phone')
        verification_code = request.data.get('verification_code')

        if serializer.is_valid():
            user = serializer.save()
            cart = Cart.objects.create(user=user)
            cart.save()
            return Response({"detail": "User successfully created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Verification"])
class VerificationView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone')
        verification_code = str(randint(1000, 9999))

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f'Your verification code: {verification_code}',
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        return Response({'verification_code': verification_code})


@extend_schema(tags=["Login"])
class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return Response({'detail': 'Invalid phone number.'}, status=status.HTTP_400_BAD_REQUEST)

        verification_code = str(randint(1000, 9999))
        refresh = RefreshToken.for_user(user)

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f'Your verification code: {verification_code}',
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone
        )

        return Response({
            'detail': 'SMS with verification code sent.',
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)


@extend_schema(tags=["ProfileChange"])
class ProfileChangeView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserProfileSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UsersListSerializer
    http_method_names = ['get', 'put', 'patch', 'delete']



