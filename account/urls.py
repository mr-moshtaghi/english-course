from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import TokenObtainPairWithoutPasswordSerializer
from .views import GetCodeView

app_name = 'account'
urlpatterns = [
    path('get-code/', GetCodeView.as_view(), name='get_code'),
    path('token/', TokenObtainPairView.as_view(serializer_class=TokenObtainPairWithoutPasswordSerializer)),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
