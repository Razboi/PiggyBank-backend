# Generated by Django 2.0.2 on 2018-02-20 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0006_auto_20180216_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
