from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers

from groups.api.serializers import ChildDisplaySerializer
from ..models import Parent, Child

User = get_user_model()


class ParentDisplaySerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    print(child)

    class Meta:
        model = User
        fields = [
            'username',
            # 'first_name',
            'child',
            'url',
            # 'email',
        ]

    def get_child(self, obj):
        request = self.context.get("request")
        user = request.user

        child_name_list = []
        try:
            if user.is_authenticated():
                parent = user.parent
                child_obj= Child.objects.filter(childs_parent=parent)
                child_name_list = [child_name.name for child_name in child_obj]
        except:
            pass
        return child_name_list

    def get_url(self, obj):
        return reverse_lazy("profile:detail", kwargs={"username": obj.username})

