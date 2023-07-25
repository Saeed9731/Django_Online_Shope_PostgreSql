from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse

from json import dumps
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
        'callback_url': '127.0.0.1:8000',
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
    return redirect('https://w3schools.com/python/demopage.htm')




    x = requests.get('https://w3schools.com/python/demopage.htm')
    print(x.text)
