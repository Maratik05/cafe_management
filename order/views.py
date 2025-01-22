from django.shortcuts import render
from .models import Order
from django.views.generic import ListView, DetailView, FormView, DeleteView
from rest_framework.generics import ListCreateAPIView
from .serializers import OrderSerializer
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Order
from .forms import AddOrder



class ListView(ListView):
    model = Order
    template_name = "order/list.html"
    context_object_name = "orders"


class DetailView(DetailView):
    model = Order
    template_name = "order/detail.html"
    pk_url_kwarg = "table_number"
    context_object_name = "order"


class AddOrder(FormView):
    template_name = 'order/form.html'
    form_class = AddOrder
    success_url = reverse_lazy('list-order')



    def form_valid(self, form):
        # Логика сохранения данных заказа
        form.save()
        return super().form_valid(form)
    

# class AddOrder(CreateView):
#     model = Order
#     template_name = "order/form.html"
#     fields = ['table_number', 'items']

    
class DeleteOrder(DeleteView):
    model = Order
    template_name = 'order/delete.html'
    success_url = reverse_lazy('list-order')
    pk_url_kwarg = 'table_number'




class OrderApiList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
    
    
