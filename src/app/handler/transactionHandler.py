import json
import os
import dotenv
import midtransclient
from django.http import JsonResponse

dotenv.load_dotenv()

class Handler:
    @staticmethod
    def get(request):
        snap = midtransclient.Snap(
            is_production=False,
            server_key=os.getenv('SERVER_KEY'),
        )

        param = {
            "transaction_details": {
                "order_id": "test2",
                "gross_amount": 20000
            }, "credit_card":{
                "secure" : True
            }, "customer_details":{
                "first_name": "budi",
                "last_name": "anakan",
                "email": "yooooshh@mail.com",
                "phone": "08111222333"
            }
        }

        transaction = snap.create_transaction(param)

        response = JsonResponse({
            'message': 'ok',
            'data': transaction
        })
        response.status_code = 200
        return response