from django.shortcuts import render
from .models import Order
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListCreateAPIView
from .serializers import OrderSerializer

# Create your views here.
class ListView(ListView):
    model = Order
    template_name = "order/list.html"
    context_object_name = "orders"


class DetailView(DetailView):
    model = Order
    template_name = "order/detail.html"
    


class OrderApiList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
    
    
