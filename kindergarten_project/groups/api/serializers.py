from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


from rest_framework import serializers
from rest_framework.reverse import reverse

from accounts.api.serializers import UserDisplaySerializer
from accounts.models import Parent
from ..models import Child, Group

User = get_user_model()


class GroupModelSerializer(serializers.ModelSerializer):
    """
    Serializer for a Group Model
    """
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


class ChildModelSerializer(serializers.ModelSerializer):
    """
    Serializer for a Child model
    """
    parent = UserDisplaySerializer(read_only=True)
    group = GroupModelSerializer(read_only=True)
    group_id = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), source='group', write_only=True)
    picture = serializers.FileField(max_length=None, allow_empty_file=True, use_url=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Child
        fields = [
            'name',
            'parent',
            'group',
            'group_id',
            'picture',
            'url',
        ]

    def get_url(self, obj):
        return reverse_lazy("child-group:child-detail", kwargs={"pk": obj.pk})

