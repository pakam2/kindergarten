from django.conf.urls import url

from .views import (
    GroupDetailView,
    ChildDetailView,
    ChildCreateView,
    ChildUpdateView,
)

urlpatterns = [
    url(r'^detail/(?P<pk>(\d)+)/$', ChildDetailView.as_view(), name='child-detail'),
    url(r'^update/(?P<pk>(\d)+)/$', ChildUpdateView.as_view(), name='child-update'),
    url(r'^create/$', ChildCreateView.as_view(), name='child-create'),
    url(r'^(?P<group_name>[\w.@+-]+)/$', GroupDetailView.as_view(), name='group-detail'),
]