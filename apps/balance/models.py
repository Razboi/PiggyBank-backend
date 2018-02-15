from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from ..users.models import Account

class Balance(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, unique=True)
    total_Balance = models.DecimalField(default=0, decimal_places=2, max_digits=20)

    def __str__(self):
        return self.user.name

class Transaction(models.Model):
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=120)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=20)

    def __str__(self):
        return str(self.date) + " | " + self.description

def add_to_balance(sender, instance, **kwargs):
    current_balance = Balance.objects.get(user=instance.balance.user)
    current_balance.total_Balance += instance.amount
    current_balance.save()
    print("final balance: " + str(current_balance.total_Balance))

post_save.connect(add_to_balance, sender=Transaction)
