from rest_framework import routers
from kindergarten_api import views as myapp_views

router = routers.DefaultRouter()
router.register(r'children', myapp_views.ChildViewset)
router.register(r'groups', myapp_views.GroupViewset)
router.register(r'profiles', myapp_views.UserViewset)
router.register(r'guardian', myapp_views.GuardianViewset)