# Generated by Django 2.0.2 on 2018-02-21 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0008_auto_20180221_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='total_Balance',
            new_name='totalBalance',
        ),
    ]
