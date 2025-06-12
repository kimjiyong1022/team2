from django.urls import path
from accounts import views


urlpatterns = [
    path("", views.AccountCreateAPIView.as_view(), name="account-create"),
    path("<int:account_id>/", views.AccountDeleteAPIView.as_view(), name="account-delete"),
]