from django.db import models

# Create your models here.

# set foreign key manually
# models.ForeignKey(TableName, on_delete=models.CASCADE, db_column='Column_name')

class Receipts(models.Model):
    id = models.CharField(max_length=16, null=False, primary_key=True, default=None)
    name = models.CharField(max_length=35, null=False, default=None)
    field = models.TextField(null=False, default=None)
    date = models.DateField(null=False, default=None)
    image = models.CharField(max_length= 200, null=False, default=None)

    def __str__(self):
        return self.id

class SubscriptionLists(models.Model):
    id = models.AutoField(primary_key=True, null=False, default=None)
    _type = models.CharField(max_length=10, null=False, default=None)
    receipt_id = models.ForeignKey(Receipts, on_delete=models.CASCADE)

    def __str__(self):
        return self._type

class SubscriptionTier(models.Model):
    id = models.AutoField(primary_key=True, null=False, default=None)
    _type = models.CharField(max_length=10, null=False, default=None)
    cost = models.PositiveIntegerField(null=False, default=None)

    def __str__(self):
        return self._type

class Client(models.Model):
    id = models.CharField(max_length=16, null=False, primary_key=True, default=None)
    email = models.CharField(max_length=25, null=False, default=None)
    username = models.CharField(max_length=30, null=False, default=None)
    password = models.CharField(max_length=20, null=False, default=None)
    phone_number = models.CharField(max_length=14, null=False, default=None)

    def __str__(self):
        return self.id
    
class Subscriptions(models.Model):
    id = models.AutoField(primary_key=True, null=False, default=None)
    _type = models.CharField(max_length=10, null=False, default=None)
    expired_date = models.DateField(null=False, default=None)
    subscriber_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, default=None)

    def __str__(self):
        return self.subscriber_id


class Transaction(models.Model):
    id = models.AutoField(primary_key=True, null=False, default=None)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, default=None)
    _type = models.CharField(max_length=10, null=False, default=None)
    date = models.DateField(null=False, default=None)

    def __str__(self):
        return self.client_id
