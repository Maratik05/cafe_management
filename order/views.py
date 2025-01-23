from .models import Order
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, FormView
from rest_framework.generics import ListCreateAPIView
from .serializers import OrderSerializer
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Order
from .forms import AddOrder
from django.db.models import Q



class ListView(ListView):
    model = Order
    template_name = "order/list.html"
    context_object_name = "orders"

    def get_queryset(self):
        """Фильтрация заказов по поисковому запросу и статусу"""
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')  # Получаем значение из поисковой строки
        if search_query:
            queryset = queryset.filter(
                Q(table_number__icontains=search_query) |  # Поиск по номеру стола
                Q(status__icontains=search_query)          # Поиск по статусу
            )
        return queryset


class DetailView(DetailView):
    model = Order
    template_name = "order/detail.html"
    pk_url_kwarg = "table_number"
    context_object_name = "order"




class UpdateOrder(UpdateView):
    model = Order
    template_name = 'order/update.html'
    context_object_name = 'order'
    pk_url_kwarg = 'table_number'
    fields = ['status']
    success_url = reverse_lazy('list-order')



class AddOrder(FormView):
    template_name = 'order/form.html'
    form_class = AddOrder
    success_url = reverse_lazy('list-order')



    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


    
class DeleteOrder(DeleteView):
    model = Order
    template_name = 'order/delete.html'
    success_url = reverse_lazy('list-order')
    pk_url_kwarg = 'table_number'




class OrderApiList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
    
    
