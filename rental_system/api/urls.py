from django.urls import include, path
from rest_framework import routers, viewsets
from . import views


router = routers.DefaultRouter()
router.register(r'rooms', views.RoomViewSet)
router.register(r'amenties', views.AmentieViewSet)
router.register(r'house_rules', views.HouseRuleViewSet)
router.register(r'locations', views.LocationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))   
]