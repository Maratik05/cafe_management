from django.db import models

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
        ('ready', 'готово'),
        ('pending','в ожидании'),
        ('paid', 'оплачено')
    ]

    table_number = models.IntegerField(unique=True,verbose_name='номер стола')
    items = models.JSONField(verbose_name='список блюд')
    total_price = models.DecimalField(verbose_name='Общая сумма', max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending',verbose_name='статус заказа')


    def calc_total_price(self):
        sum(item['price']for item in self.items)

    def get_status_order(self):
        return self.status     
        
    def save(self,*args,**kwargs):
            self.calc_total_price()
            super().save(args,kwargs)

    def __str__(self):
         return 'Заказ {self.id} - номер стола {self.table_number} ({self.get_status_order})'