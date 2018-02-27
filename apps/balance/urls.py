from django.urls import path
from .views import (TransactionsCreateView, BalanceRetrieveView, AllTransactionsView,
CreateTransaction, UpdateTransaction)
from rest_framework.authtoken import views

app_name = "balance"

urlpatterns = [
    path("", TransactionsCreateView.as_view(), name="transactions-create"),
    path("all-transactions", AllTransactionsView.as_view(), name="all-transactions"),
    path("create-transaction", CreateTransaction.as_view(), name="create-transaction"),
    path("update-transaction", UpdateTransaction.as_view(), name="update-transaction"),
    path("total", BalanceRetrieveView.as_view(), name="balance-retrieve"),
]
