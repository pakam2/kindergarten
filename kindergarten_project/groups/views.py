from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
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


class ChildCreateView(LoginRequiredMixin, CreateView):
    form_class = ChildForm
    template_name = 'groups/child_form.html'
    # success_url = 'child-group:child-detail'

    # assigning child to logged in user/parent
    def form_valid(self, form):
        obj = form.save(commit=True)
        parent = Parent.objects.get(name_of_parent=self.request.user)
        parent.child.add(obj)
        return super(ChildCreateView, self).form_valid(form)


class ChildUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ChildForm
    template_name = 'groups/child_form.html'

    def get_queryset(self):
        return Child.objects.all()


class ChildDeleteView(LoginRequiredMixin, DeleteView):
    model = Child
    template_name = 'groups/confirm_delete.html'
    success_url = reverse_lazy("main")


class GroupDetailView(LoginRequiredMixin, DetailView):
    template_name = 'groups/group_detail_view.html'
    queryset = Group.objects.all()

    def get_object(self):
        return get_object_or_404(
                    Group,
                    group_name__iexact=self.kwargs.get("group_name")
                    )


class GroupListView(LoginRequiredMixin, ListView):
    template_name = 'groups/group_list_view.html'

    def get_queryset(self):
        return Group.objects.all()