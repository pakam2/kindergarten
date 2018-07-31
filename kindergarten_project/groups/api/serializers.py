from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


from rest_framework import serializers
from rest_framework.reverse import reverse

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

    group = GroupModelSerializer(read_only=True)
    group_id = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), source='group', write_only=True)
    url = serializers.SerializerMethodField ()

    class Meta:
        model = Child
        fields = [
            'name',
            'group',
            'group_id',
            'url',
        ]

    def get_url(self, obj):
        return reverse_lazy("child-group:child-detail", kwargs={"pk": obj.pk})

