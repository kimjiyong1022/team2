from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView

from users.views import UserSignupAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('logout/', TokenBlacklistView.as_view()),
    path('signup/', UserSignupAPIView.as_view()),
]