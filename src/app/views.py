from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .handler.userHandler import Handler as userHandler
from .handler.receiptHandler import Handler as receiptHandler
# from rest_framework import serializers

# Create your views here.
def Homepage(request):
    return HttpResponse(loader.get_template('homepage.html').render())

def BaseDirApi(request):
    return HttpResponse(loader.get_template('baseapi.html').render())

def User(request):
    if request.method == 'GET':
        return userHandler.getUser(request)
    elif request.method == 'POST':
        return userHandler.createUser(request)
    elif request.method == 'PUT':
        return userHandler.updateUser(request)
    elif request.method == 'DELETE':
        return userHandler.deleteUser(request)
    else:
        return HttpResponse("No Api Initialized!")

def Receipt(request):
    if request.method == 'GET':
        receiptId = request.GET.get('id', '')
        if receiptId != '':
            return receiptHandler.getReceiptById(receiptId)
        else:
            return receiptHandler.getReceiptAll(request)