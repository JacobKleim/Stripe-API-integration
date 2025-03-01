from django.urls import path

from . import views

urlpatterns = [
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),
    path('item/<int:item_id>/', views.item_details, name='item_details'),
    path('order_items/<int:order_id>/', views.order_items, name='order_items'),
    path('buy_order/<int:order_id>/', views.buy_items, name='buy_order'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]