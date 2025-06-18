from django.urls import path
from accounts import views
from accounts.views import AccountDetailAPIView

urlpatterns = [
    path("create/", views.AccountCreateAPIView.as_view(), name="account-create"),
    path("<int:account_id>/", views.AccountDeleteAPIView.as_view(), name="account-delete"),
    path('api/accounts/<int:account_id>/', AccountDetailAPIView.as_view(), name='account-detail'),

    # path("<int:account_id>/", TransactionListByAccountAPIView.as_view()),
]