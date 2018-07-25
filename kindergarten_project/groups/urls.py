from django.conf.urls import url

from .views import (
    ChildDetailView,
    ChildCreateView,
    ChildUpdateView,
    ChildDeleteView,
    GroupDetailView,
    GroupListView,
)

urlpatterns = [
    url(r'^detail/(?P<pk>(\d)+)/$', ChildDetailView.as_view(), name='child-detail'),
    url(r'^update/(?P<pk>(\d)+)/$', ChildUpdateView.as_view(), name='child-update'),
    url(r'^create/$', ChildCreateView.as_view(), name='child-create'),
    url(r'^delete/(?P<pk>(\d)+)/$', ChildDeleteView.as_view(), name='child-delete'),
    url(r'^group-list/$', GroupListView.as_view(), name='group-list'),
    url(r'^(?P<group_name>[\w.@+-]+)/$', GroupDetailView.as_view(), name='group-detail'),

]