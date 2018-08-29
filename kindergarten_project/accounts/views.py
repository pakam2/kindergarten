from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View

from groups.forms import ChildForm
from accounts.models import Parent, Guardian
from groups.models import Child, Group

User = get_user_model()


# class ParentDetailView(DetailView):
#     template_name = 'accounts/parent_detail_view.html'
#     queryset = User.objects.all()
#
#     def get_object(self):
#         username = self.kwargs.get('username')
#         if username is None:
#             raise Http404
#         return get_object_or_404(
#             User,
#             username__iexact=username,
#             # is_active=True
#         )


class ParentDetailView(View):
    def get(self, request, username):
        username = username
        form = ChildForm
        ctx = {
            'form': form,
            'username': username,
        }
        return render(request, 'accounts/parent_detail_view.html', ctx)

