from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from accounts.models import Parent
from ..models import Child, Group
from .serializers import GroupModelSerializer, ChildModelSerializer

User = get_user_model()


class ChildDisplayAPIView(generics.ListAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ChildCreateAPIView(generics.CreateAPIView):
    serializer_class = ChildModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     parent = Parent.objects.get(name_of_parent=user)
    #     serializer.save(childs_parent=parent)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class GroupDisplayAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupCreateAPIView(generics.CreateAPIView):
    serializer_class = GroupModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


