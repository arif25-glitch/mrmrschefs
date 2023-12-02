from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .handler.userHandler import Handler as userHandler
from .handler.receiptHandler import Handler as receiptHandler
from .handler.transactionHandler import Handler as transactionHandler

from django.views.decorators.csrf import csrf_exempt

# from rest_framework import serializers

# Create your views here.
def Homepage(request):
    return HttpResponse(loader.get_template('homepage.html').render())

def BaseDirApi(request):
    return HttpResponse(loader.get_template('baseapi.html').render())

@csrf_exempt
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

@csrf_exempt
def Transaction(request):
    if request.method == 'POST':
        return transactionHandler.get(request)
    else:
        return HttpResponse("No Api Method Initialized!")

def Receipt(request):
    if request.method == 'GET':
        receiptId = request.GET.get('id', '')
        if receiptId != '':
            return receiptHandler.getReceiptById(receiptId)
        else:
            return receiptHandler.getReceiptAll(request)