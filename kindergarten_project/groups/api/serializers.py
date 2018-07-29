from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers
from ..models import Child, Group

User = get_user_model()


class GroupDisplaySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = [
            'group_name',
            'type_of_group',
            'url',
            # 'email',
        ]

    def get_url(self, obj):
        return reverse_lazy("child-group:group-detail", kwargs={"group_name": obj.group_name})


class ChildDisplaySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    group = GroupDisplaySerializer(read_only=True)

    class Meta:
        model = Child
        fields = [
            'name',
            'group',
            'url',
        ]

    def get_url(self, obj):
        return reverse_lazy("child-group:child-detail", kwargs={"pk": obj.pk})