from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers

# from groups.api.serializers import ChildModelSerializer, GroupModelSerializer
from ..models import Parent, Child

User = get_user_model()


class ParentDisplaySerializer(serializers.ModelSerializer):
    name_of_parent = serializers.SerializerMethodField()
    # child = ChildModelSerializer(many=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Parent
        fields = [
            'name_of_parent',
            # 'first_name',
            # 'child',
            'url',
            # 'email',
        ]

    def get_name_of_parent(self, obj):
        request = self.context.get('request')
        username = request.user.username
        return username

    def get_url(self, obj):
        return reverse_lazy("profile:detail", kwargs={"username": obj.name_of_parent})


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