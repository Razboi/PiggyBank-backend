from django.urls import path
from .views import TransactionsCreateView, BalanceRetrieveView, AllTransactionsView
from rest_framework.authtoken import views

app_name = "balance"

urlpatterns = [
    path("", TransactionsCreateView.as_view(), name="transactions-create"),
    path("all-transactions", AllTransactionsView.as_view(), name="all-transactions"),
    path("total", BalanceRetrieveView.as_view(), name="balance-retrieve"),
]
