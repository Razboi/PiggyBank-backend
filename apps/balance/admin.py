from django.contrib import admin
from .models import Balance, Transaction

admin.site.register(Transaction)
admin.site.register(Balance)
