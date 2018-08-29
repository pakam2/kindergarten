from django.urls import reverse_lazy
from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Parent, Guardian
from groups.models import Child, Group

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'group_name', 'type_of_group')


class UserDisplaySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'url',
        ]

    def get_url(self, obj):
        return reverse_lazy("profile:detail", kwargs={"username": obj.username})


class ChildSerializer (serializers.ModelSerializer):
    parent = UserDisplaySerializer(read_only=True)

    class Meta:
        model = Child
        fields = ('id', 'name', 'group', 'parent', 'picture', 'url')

    def get_url(self, obj):
        return reverse_lazy ("child-group:child-detail", kwargs={"pk": obj.pk})


class GuardianSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)

    class Meta:
        model = Guardian
        fields = ('id', 'user', 'parent', 'group')



