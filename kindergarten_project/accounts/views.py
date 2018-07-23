from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from accounts.models import Parent, Guardian
from groups.models import Child, Group

User = get_user_model()


class ParentDetailView(DetailView):
    template_name = 'accounts/parent_detail_view.html'
    queryset = User.objects.all()

    def get_object(self):
        username = self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(
            User,
            username__iexact=username,
            is_active=True
        )

    def get_context_data(self, *args, **kwargs):
        context = super(ParentDetailView, self).get_context_data(*args, **kwargs)
        parent = Parent.objects.get(name_of_parent=self.get_object())
        context['children'] = Child.objects.filter(childs_parent=parent)
        return context



