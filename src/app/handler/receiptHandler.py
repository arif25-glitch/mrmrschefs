from django.http import JsonResponse
from django.core import serializers
from ..models import Receipts
import json

class Handler:
    @staticmethod
    def getReceiptById(receiptId):
        try:
            data = json.loads(serializers.serialize('json', [Receipts.objects.get(id=receiptId)]))[0]['fields']
            response = JsonResponse({
                'status': 'success',
                'data': data,
            })
            response.status_code = 200
            return response
        except:
            response = JsonResponse({
                'status': 'fail',
                'id': receiptId,
            })
            response.status_code = 404
            return response

    
    def getReceiptAll(request):
        try:
            data = []
            for i in Receipts.objects.all():
                temp = json.loads(serializers.serialize('json', [i]))[0]
                data.append({
                    'id': temp['pk'],
                    'data': temp['fields']
                })
            response = JsonResponse({
                'status': 'success',
                'data': data
            })
            response.status_code = 200
            return response
        except:
            response = JsonResponse({
                'status': 'fail',
                'message': 'Internal server error'
            })
            response.status_code = 500
            return response