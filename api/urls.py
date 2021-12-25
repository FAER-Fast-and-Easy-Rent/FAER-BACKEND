from django.urls import include, path
from rest_framework import routers, viewsets
from . import views


router = routers.DefaultRouter()
router.register(r'rooms', views.RoomViewSet)
router.register(r'amenties', views.AmentieViewSet)
router.register(r'house_rules', views.HouseRuleViewSet)
router.register(r'locations', views.LocationViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', include(router.urls)),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
