from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from .models import User
from .serializers import UserSerializer
from .utils import rando_username


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        email = request.data['email']
        password = request.data['password']

        if User.objects.filter(email=email).exists():
            return Response({
                'msg': _('User already exists!'),
                'status': status.HTTP_400_BAD_REQUEST
            })
        else:
            new_user = User.objects.create_user(
                    username=rando_username(),
                    name=name, email=email)
            new_user.set_password(password)
            new_user.save()
            return Response({
                'msg': _('User successfully registered!'),
                'token': new_user.auth_token.key,
                'status': status.HTTP_201_CREATED
            })


class UserLogin(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']

        if not email or not password:
            return Response({
                'msg': _('Enter the data correctly!'),
                status: status.HTTP_400_BAD_REQUEST
            })
        elif User.objects.filter(email=email).exists():
            user = authenticate(password=password, username=email)
            if user:
                return Response({
                    'email': user.email,
                    'name': user.name,
                    'token': user.auth_token.key,
                    'status': status.HTTP_200_OK
                })
            else:
                return Response({
                    'msg': _('Invalid email or password'),
                    'status': status.HTTP_400_BAD_REQUEST
                })
        else:
            return Response({
                'msg': _('There is no user registered with this data!'),
                'status': status.HTTP_400_BAD_REQUEST
            })