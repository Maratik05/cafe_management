from django.urls import include, path
from .views import ListView, DetailView, AddOrder, DeleteOrder, UpdateOrder, OrderViewSet, CalcRevenueView
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(r'order', OrderViewSet, basename='order')


urlpatterns = [
    path('', ListView.as_view(), name='list-order'),
    path('<int:table_number>/', DetailView.as_view(), name='detail-order'),
    path('add_order/', AddOrder.as_view(), name='add-order'),
    path('update_order/<int:table_number>', UpdateOrder.as_view(), name='update-order'),
    path('delete_order/<int:table_number>', DeleteOrder.as_view(),name='del-order'),
    path('api/', include(router.urls)),
    path('calc_revenue/', CalcRevenueView.as_view(), name='calc-revenue'),

]
