from django.conf.urls import url

from .views import (
    ChildDisplayAPIView,
    ChildCreateAPIView,
    ChildModelViewsetView,
    GroupDisplayAPIView,
    GroupCreateAPIView,
)

urlpatterns = [
    # url(r'^child-create/$', ChildCreateAPIView.as_view(), name='child-create'),
    url(r'^child-create/$', ChildModelViewsetView.as_view({
            'post': 'create',
            'get': 'list',
        }), name='child-create'),
    url(r'^child-list/$', ChildDisplayAPIView.as_view(), name='child-list'),
    url(r'^group-list/$', GroupDisplayAPIView.as_view(), name='group-list'),
    url(r'^group-create/$', GroupCreateAPIView.as_view(), name='group-create'),

]