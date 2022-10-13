from sharks_api.models import Order
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.


class OrdersTable(ListView):
    paginate_by = 10
    model = Order
    context_object_name = 'Orders'
    template_name = 'orders.html'



class OrdersbyBrand(ListView):
    paginate_by = 10
    model = Order
    context_object_name = 'Orders'
    template_name = 'orders.html'

    def get_queryset(self):
        return Order.objects.filter(brand=self.kwargs['brand_id'])