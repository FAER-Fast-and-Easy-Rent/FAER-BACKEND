from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register(r'rooms', views.RoomViewSet.as_view({'get': 'list','post':'create'}))

urlpatterns = [
    # path('', include(router.urls)),
    path('rooms/', views.RoomViewSet.as_view({'get': 'list','post':'create'})),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/user/', include('accounts.urls')),
    path('test', views.TestViewSet.as_view({'get': 'list','post':'create'})),
]
