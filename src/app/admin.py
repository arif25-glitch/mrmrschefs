from django.contrib import admin
from .models import Receipts, SubscriptionLists, SubscriptionTier, Subscriptions, Client, Transaction

# Register your models here.

class ListReceipts(admin.ModelAdmin):
    list_display = ('id', 'name')
class ListClient(admin.ModelAdmin):
    list_display = ('id', 'email', 'username')
    search_fields = ['username']
class ListSubscriptionLists(admin.ModelAdmin):
    list_display = ('id', '_type', 'receipt_id')
# class ListSubscriptionTier(admin.ModelAdmin):
#     list_display = ('id', '_type', 'cost')

admin.site.register(Receipts, ListReceipts)
admin.site.register(SubscriptionLists, ListSubscriptionLists)
admin.site.register(SubscriptionTier)
admin.site.register(Subscriptions)
admin.site.register(Client, ListClient)
admin.site.register(Transaction)