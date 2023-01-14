from rest_framework import routers
from mainApp import views

router = routers.DefaultRouter()
router.register(r'account', views.AccountViewSet)
urlpatterns = router.urls