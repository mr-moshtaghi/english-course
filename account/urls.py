from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import TokenObtainPairWithoutPasswordSerializer
from .views import TestView

app_name = 'account'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(serializer_class=TokenObtainPairWithoutPasswordSerializer)),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', TestView.as_view({'get': 'list'}))
]
