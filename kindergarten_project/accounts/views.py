from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import Parent, Teacher

User = get_user_model()


class ParentDetailView(DetailView):
    template_name = 'accounts/parent_detail_view.html'
    queryset = Parent.objects.all()

    def get_object(self):
        return get_object_or_404(
                    Parent,
                    first_name__iexact=self.kwargs.get("first_name")
                    )
