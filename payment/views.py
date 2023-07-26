import json

from django.shortcuts import redirect, reverse, get_object_or_404
from django.conf import settings
from django.http import HttpResponse

import requests
from orders.models import Order


def payment_process(request):
    # get order id from session
    orders_id = request.session.get('order_id')
    # get order object
    order = get_object_or_404(Order, id=orders_id)

    toman_total_price = order.get_total_price()
    rial__total_price = toman_total_price * 10

    zarinpal_request_url = ''

    requests_header = {
        "accept": "application/json",
        "content-type": "application/json",
    }
    request_data = {
        'merchant_id': settings.ZARINAPAL_MERCHANT_ID,
        'amount': rial__total_price,
        'description': f'#{order.id}: {order.user.first_name} {order.user.last_name}',
        'callback_url': request.build_absolute_uri(reverse('payment:payment_callback')),
    }

    # res = requests.post(url=zarinpal_request_url, data=dumps(request_data), headers=requests_header)
    # data = res.json()['data']
    # authority = data['authority']
    # order.zarinpal_authority = authority
    # order.save()
    #
    # if 'errors' not in data or len(data['errors']) == 0:
    #     return redirect(f'...zarinpall...{authority}')
    # else:
    #     return HttpResponse('Error from zarinpal!!!')
    x = requests.get('https://w3schools.com/python/demopage.htm')
    print(x.text)
    return redirect('https://w3schools.com/python/demopage.htm')


def payment_callback(request):
    payment_authority = request.GET.get('Authority')
    payment_status = request.GET.get('Status')
    order = get_object_or_404(Order, zarinpal_authority=payment_authority)

    toman_total_price = order.get_total_price()
    rial__total_price = toman_total_price * 10

    if payment_status == 'OK':
        requests_header = {
            "accept": "application/json",
            "content-type": "application/json",
        }
        request_data = {
            'merchant_id': settings.ZARINAPAL_MERCHANT_ID,
            'amount': rial__total_price,
            'authority': payment_authority,
        }

        res = requests.post(
            url='',
            data=json.dumps(request_data),
            headers=requests_header,
        )

        if 'data' in res.json() and ('errors' not in res.json()['data'] or len(res.json()['data']['errors']) == 0):
            data = res.json()['data']
            payment_code = data['code']

            if payment_code == 100:
                order.is_paid = True
                order.zarinpal_ref_id = data['ref_id']
                order.zarinpal_data = data
                order.save()
                return HttpResponse('your Transaction was successful')
            elif payment_code == 101:
                return HttpResponse('This Transaction has already been registered by you')
            else:
                error_code = res.json()['errors']['code']
                error_message = res.json()['errors']['message']
                return HttpResponse(
                    f'Transaction failed !!! \t error code: {error_code} \t error message: {error_message}')
        else:
            error_code = res.json()['errors']['code']
            error_message = res.json()['errors']['message']
            return HttpResponse(
                f'Transaction failed !!! \t error code: {error_code} \t error message: {error_message}')
    else:
        return HttpResponse(f'Transaction failed !!!')
