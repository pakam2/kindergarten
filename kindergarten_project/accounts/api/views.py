from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from ..models import Parent
from .serializers import ParentDisplaySerializer

User = get_user_model()


class ParentDisplayAPIView(generics.RetrieveUpdateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentDisplaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


