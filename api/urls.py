from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import views

urlpatterns = [
    path('auth/user/', include('accounts.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rooms/', views.RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='rooms'),
]
