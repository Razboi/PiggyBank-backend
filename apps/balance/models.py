from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from ..users.models import Account

class Balance(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, unique=True)
    totalBalance = models.DecimalField(default=0, decimal_places=2, max_digits=20)

    def __str__(self):
        return self.user.name

class Transaction(models.Model):
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=120)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    currentTotal = models.DecimalField(default=0, decimal_places=2, max_digits=20)

    def __str__(self):
        return str(self.date) + " | " + self.description + " | " + str(self.amount)

    # When creating a transaction add the current balance +- operation amount to
    # the transaction_balance
    def save(self, *args, **kwargs):
        self.currentTotal = self.balance.totalBalance + self.amount
        super(Transaction, self).save(*args, **kwargs)

def add_to_balance(sender, instance, **kwargs):
    account_balance = Balance.objects.get(user=instance.balance.user)
    account_balance.totalBalance += instance.amount
    account_balance.save()

post_save.connect(add_to_balance, sender=Transaction)
