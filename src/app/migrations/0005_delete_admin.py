# Generated by Django 4.2.6 on 2023-10-28 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_client_receipts_subscriptionlists_subscriptiontier_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
    ]