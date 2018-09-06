import json
from datetime import datetime

from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from banking.models import Transaction


@api_view(['POST'])
def save_transaction(request):
    resp, code = {}, 200
    if request.method == 'GET':
        resp = {'error': 'Not allowed'}
        code = 404

    try:
        json_body = json.loads(request.body)
    except ValueError as e:
        resp = {'error': 'Invalid request body'}
        code = 400
    else:
        source = json_body.get('from_service_name')
        service_data = json_body.get('data')
        type = service_data.get('type')
        transaction_data = service_data.get('data')
        created_on = transaction_data.get('created_at')
        user_email = transaction_data.get('user_email')
        inc_id = transaction_data.get('inc_id')
        transaction_id = transaction_data.get('transaction_id')
        amount = transaction_data.get('amount')
        action = transaction_data.get('action')

        try:
            Transaction.objects.create(modified_at=datetime.now(), action=action, amount=amount, source_service=source, type=type,
                                       created_at=created_on, user_email=user_email, transaction_id=transaction_id, increment_id=inc_id)
            resp = {'success': True}
        except IntegrityError as e:
            resp = {'error': e.message}

    return HttpResponse(json.dumps(resp), content_type='application/json', status=code)

@api_view(['GET'])
def list_all(request):
    transactions = Transaction.objects.all()
