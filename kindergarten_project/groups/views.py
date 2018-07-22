from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Group, Child

User = get_user_model()


class ChildDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/child_detail_view.html'
    queryset = Child.objects.all()

    def get_object(self):
        return get_object_or_404(
                    Child,
                    name__iexact=self.kwargs.get("child_name")
                    )


class GroupDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/group_detail_view.html'
    queryset = Group.objects.all()

    def get_object(self):
        return get_object_or_404(
                    Group,
                    group_name__iexact=self.kwargs.get("group_name")
                    )
