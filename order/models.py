from django.db import models
from django.urls import reverse

# Create your models here.

class Order(models.Model):
    
    
    STATUS_CHOICES = [
        ('готово', 'готово'),
        ('в ожидании','в ожидании'),
        ('оплачено', 'оплачено') 
        ]
    table_number = models.IntegerField(unique=True,verbose_name='номер стола')
    items = models.JSONField(verbose_name='список блюд') 
    total_price = models.DecimalField(verbose_name='Общая сумма', max_digits=10, decimal_places=2, default=0)       
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='в ожидании',verbose_name='статус заказа')

    def calc_total_price(self):
        return sum(item['price'] for item in self.items)

    def get_status_order(self):
        return self.status   
    def format_items(items):
    
        return "\n".join(f"{item['name']} - {item['price']}" for item in items)
    
    def get_table_number(self):
        return self.table_number
      
   
      
    def save(self,*args,**kwargs):
            self.total_price = self.calc_total_price()
            super().save(args,kwargs)

    def __str__(self):
         return f'Заказ {self.pk} - номер стола {self.table_number} ({self.status})'
    
    def get_absolute_url(self):
        return reverse("order-detail", kwargs={"pk": self.pk})
    