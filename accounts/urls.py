from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from django.urls import path

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login-view'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-view'),
    path('verify/', TokenVerifyView.as_view(), name='verify-token')
]
