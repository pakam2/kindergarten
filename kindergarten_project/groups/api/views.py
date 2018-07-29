from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from ..models import Child, Group
from .serializers import GroupDisplaySerializer, ChildDisplaySerializer

User = get_user_model()


class GroupDisplayAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDisplaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ChildDisplayAPIView(generics.ListAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildDisplaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]