from django.urls import path
from .views import OrderApiList, ListView, DetailView, AddOrder, DeleteOrder, UpdateOrder


urlpatterns = [
    path('', ListView.as_view(), name='list-order'),
    path('<int:table_number>/', DetailView.as_view(), name='detail-order'),
    path('add_order/', AddOrder.as_view(), name='add-order'),
    path('update_order/<int:table_number>', UpdateOrder.as_view(), name='update-order'),
    path('delete_order/<int:table_number>', DeleteOrder.as_view(),name='del-order'),
    path('api/', OrderApiList.as_view(), name='list-order-api'),

]
