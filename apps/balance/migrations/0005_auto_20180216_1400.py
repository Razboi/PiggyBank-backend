# Generated by Django 2.0.2 on 2018-02-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0004_auto_20180215_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
