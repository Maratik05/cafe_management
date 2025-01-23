from django import forms
from .models import Order


class AddOrder(forms.ModelForm):
    table_number = forms.IntegerField(label="Номер стола")
    items = forms.CharField(
        label="Блюда",
        widget=forms.Textarea(attrs={'placeholder': 'Введите блюда и цены в формате: \nНазвание1 - Цена1\nНазвание2 - Цена2', 'rows': 7, 'cols': 30}),
        required=True
    )

    class Meta:
        model = Order
        fields = ['table_number', 'items']

    def clean_items(self):
        
        items_raw = self.cleaned_data['items']
        items_list = []
        try:
            for line in items_raw.splitlines():
                name, price = line.split('-')
                items_list.append({'name': name.strip(), 'price': float(price.strip())})
        except ValueError:
            raise forms.ValidationError("Введите данные в формате: Название - Цена (каждая пара на новой строке)")
        return items_list

