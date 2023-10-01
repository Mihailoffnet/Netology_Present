from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from demo.models import Adv
from django.contrib.auth.models import User
from demo.permissions import IsOwnerOrReadOnly
from demo.serializers import AdvSerializer, UserSerializer


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] # если только IsAuthenticated, то все действия имеет право любой юзер с аутентификацией
    permission_classes = [IsOwnerOrReadOnly] #выполнять действия могут все даже без аутентификации
    throttle_classes = [AnonRateThrottle]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


