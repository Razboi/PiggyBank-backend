# Generated by Django 2.0.2 on 2018-02-15 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0002_auto_20180215_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]
