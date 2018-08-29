from django.shortcuts import render
from rest_framework import viewsets, generics
from django.views import generic
from django.contrib.auth import get_user_model

from accounts.models import Parent, Guardian
from groups.models import Child, Group
from . import serializers

User = get_user_model()


class ChildViewset(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = serializers.ChildSerializer

    def perform_create(self, serializer):
        serializer.save(parent=self.request.user)


class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserDisplaySerializer


class GuardianViewset(viewsets.ModelViewSet):
    queryset = Guardian.objects.all()
    serializer_class = serializers.GuardianSerializer


