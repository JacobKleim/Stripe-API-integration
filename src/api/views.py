from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

import stripe

from .models import Item, Order


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


def buy_item(request, item_id):
    try:
        item = get_object_or_404(Item, id=item_id)

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success/',
            cancel_url='http://localhost:8000/cancel/',
        )

        return JsonResponse({'id': session.id})

    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)


def item_details(request, item_id):
    try:

        item = get_object_or_404(Item, id=item_id)

        return render(request, 'item_details.html', {
            'item': item,
            'stripe_test_public_key': settings.STRIPE_TEST_PUBLIC_KEY
        })

    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)


def order_items(request, order_id):
    try:
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'order.html', {
            'order': order,
            'stripe_test_public_key': settings.STRIPE_TEST_PUBLIC_KEY
        })

    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)


def buy_items(request, order_id):
    try:
        order = get_object_or_404(Order, id=order_id)
        order_items = order.items.all()

        line_items = [{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        } for item in order_items]
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url='http://localhost:8000/success/',
            cancel_url='http://localhost:8000/cancel/',
        )
        return JsonResponse({'id': session.id})

    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')
