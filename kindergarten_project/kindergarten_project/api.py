from rest_framework import routers
from groups.api import views as myapp_views

router = routers.DefaultRouter()
router.register(r'child', myapp_views.ChildModelViewsetView)
# router.register(r'belongings', myapp_views.BelongingViewset)
# router.register(r'borrowings', myapp_views.BorrowedViewset)