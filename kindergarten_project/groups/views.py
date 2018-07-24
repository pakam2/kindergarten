from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Parent, Guardian
from groups.models import Group, Child
from .forms import ChildForm

User = get_user_model()


class ChildDetailView(LoginRequiredMixin, DetailView):
    template_name = 'groups/child_detail_view.html'
    queryset = Child.objects.all()

    def get_object(self):
        return get_object_or_404(
                    Child,
                    pk=self.kwargs.get("pk")
                    )


class GroupDetailView(LoginRequiredMixin, DetailView):
    template_name = 'groups/group_detail_view.html'
    queryset = Group.objects.all()

    def get_object(self):
        return get_object_or_404(
                    Group,
                    group_name__iexact=self.kwargs.get("group_name")
                    )


class ChildCreateView(LoginRequiredMixin, CreateView):
    form_class = ChildForm
    template_name = 'groups/child_form.html'
    # success_url = 'child-group:child-detail'

    def form_valid(self, form):
        obj = form.save(commit=True)
        parent = Parent.objects.get(name_of_parent=self.request.user)
        parent.child.add(obj)
        return super(ChildCreateView, self).form_valid(form)



