from rest_framework import generics, mixins
from .serializers import TransactionSerializer
from .models import Transaction, Balance
from ..users.models import Account
from rest_framework.fields import CurrentUserDefault

class TransactionsCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = "pk"
    serializer_class = TransactionSerializer

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        balance = Balance.objects.get(user=account)
        qs = Transaction.objects.filter(balance=balance)
        return qs

    def perform_create(self, serializer):
        account = Account.objects.get(user=self.request.user)
        balance = Balance.objects.get(user=account)
        serializer.save(balance=balance)

# using mixins to add the post method on the listAPIview
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
