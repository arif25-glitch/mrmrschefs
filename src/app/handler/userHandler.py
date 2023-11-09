from django.http import JsonResponse
from django.core import serializers
from ..models import Client
from nanoid import generate
import json

class Handler:
    @staticmethod
    def getUser(request):
        try:
            userid = request.GET.get('userid', '')
            data = json.loads(serializers.serialize('json', [Client.objects.get(id=userid)]))[0]['fields']
            response = JsonResponse({
                'status': 'success',
                'data': data,
            })
            response.status_code = 200
            return response
        except:
            response = JsonResponse({
                'status': 'fail',
                'id': 'User id cannot be found - ' + userid,
            })
            response.status_code = 404
            return response

    def createUser(request):
        data = json.loads(request.body.decode('utf-8'))
        id = generate(size=16)
        try:
            Client(id=id, email=data['email'], username=data['username'], password=data['password'], phone_number=data['phone_number']).save()
            response = JsonResponse({
                'status': 'success',
                'id' : id,
            })
            response.status_code = 200
            return response
        except:
            response = JsonResponse({
                'status': 'fail',
                'id': id,
            })
            response.status_code = 400
            return response
    
    def updateUser(request):
        data = json.loads(request.body.decode('utf-8'))
        userid = request.GET.get('userid', '')
        try:
            x = Client.objects.get(id=userid)
            oldData = json.loads(serializers.serialize('json', [x]))[0]['fields']

            x.email = data['email']
            x.password = data['password']
            x.username = data['username']
            x.phone_number = data['phone_number']

            newData = json.loads(serializers.serialize('json', [x]))[0]['fields']
            x.save()

            response = JsonResponse({
                'status': 'success',
                'id': userid,
                'oldData': oldData,
                'newData': newData,
            })
            response.status_code = 200
            return response
        except:
            response = JsonResponse({
                'status': 'fail',
                'id': userid,
            })
            response.status_code = 400
            return response
        
    def deleteUser(request):
        userid = request.GET.get('userid', '')
        try:
            x = Client.objects.get(id=userid)
            x.delete()

            response = JsonResponse({
                'status': 'success',
                'id': userid,
            })
            response.status_code = 200
            return response
        except:
            response = JsonResponse({
                'status': 'fail',
                'id': userid
            })
            response.status_code = 404
            return response