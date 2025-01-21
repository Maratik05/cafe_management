from django.urls import path
from .views import OrderApiList, ListView


urlpatterns = [
    path('', ListView.as_view(), name='list-order'),

]
