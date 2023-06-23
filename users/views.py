from rest_framework import generics, status, viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Cart
from .serializers import LoginSerializer, RegisterSerializer, UserProfileSerializer, UsersListSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            cart = Cart.objects.create(user=user)
            cart.save()

            return Response({"detail": "User successfully created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

        refresh = RefreshToken.for_user(user)
        return Response({
            'detail': 'вы успешно вошли',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


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


