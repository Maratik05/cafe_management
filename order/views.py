from .models import Order
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, FormView, TemplateView
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer
from django.urls import reverse_lazy
from .models import Order
from .forms import AddOrderForm, UpdateOrderForm
from django.db.models import Q, Sum



class ListView(ListView):
    model = Order
    template_name = "order/list.html"
    context_object_name = "orders"

    def get_queryset(self):
        
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')  
        if search_query:
            queryset = queryset.filter(
                Q(table_number__icontains=search_query) |  
                Q(status__icontains=search_query)         
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
    form_class = UpdateOrderForm
    pk_url_kwarg = 'table_number'  
    success_url = reverse_lazy('list-order')
    
    

    def form_valid(self, form):
      
        form.instance.items = form.cleaned_data['items']
        return super().form_valid(form)
    
   
    
    
        




class AddOrder(FormView):
    template_name = 'order/form.html'
    form_class = AddOrderForm
    success_url = reverse_lazy('list-order')



    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


    
class DeleteOrder(DeleteView):
    model = Order
    template_name = 'order/delete.html'
    success_url = reverse_lazy('list-order')
    pk_url_kwarg = 'table_number'

   


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
    

class CalcRevenueView(TemplateView):
    template_name = "order/calc_revenue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paid_orders = Order.objects.filter(status="оплачено")
        total_revenue = paid_orders.aggregate(Sum('total_price'))['total_price__sum'] or 0
        context['total_revenue'] = total_revenue
        context['paid_orders'] = paid_orders
        return context

    
    


    
    
    
    
