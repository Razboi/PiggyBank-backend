from django.urls import path
from .views import TransactionsCreateView, BalanceRetrieveView
from rest_framework.authtoken import views

app_name = "balance"

urlpatterns = [
    path("", TransactionsCreateView.as_view(), name="transactions-create"),
    path("total", BalanceRetrieveView.as_view(), name="balance-retrieve"),
]
