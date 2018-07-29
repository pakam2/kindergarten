from django.conf.urls import url

from .views import ParentDisplayAPIView

urlpatterns = [
    url(r'^$', ParentDisplayAPIView.as_view(), name='list'),
]