from django import forms
from django.forms import formset_factory
from .models import Order
# class ItemForm(forms.Form):
#     name = forms.CharField(label="Название блюда", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     price = forms.DecimalField(label="Цена блюда", max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))

# class OrderForm(forms.Form):
#     table_number = forms.IntegerField(label="Номер стола", widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     status = forms.ChoiceField(
#         label="Статус заказа",
#         choices=[('pending', 'В ожидании'), ('ready', 'Готово'), ('paid', 'Оплачено')],
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )



# ItemFormSet = formset_factory(ItemForm, extra=1) 

class AddOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number','items']
