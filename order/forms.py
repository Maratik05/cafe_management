from django import forms
from .models import Order


class AddOrderForm(forms.ModelForm):
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
        table_number = self.cleaned_data.get('table_number')
        if table_number <= 0:
            raise forms.ValidationError("Номер стола должен быть положительным числом.")
        items_raw = self.cleaned_data['items']
        items_list = []
        try:
            for line in items_raw.splitlines():
                name, price = line.split('-')
                items_list.append({'name': name.strip(), 'price': float(price.strip())})
        except ValueError:
            raise forms.ValidationError("Введите данные в формате: Название - Цена (каждая пара на новой строке)")

        if len(items_list) == 0:
            raise forms.ValidationError("Список блюд пуст. Добавьте хотя бы одно блюдо.")
        return items_list
    

class UpdateOrderForm(forms.ModelForm):
    items = forms.CharField(
        label="Блюда",
        widget=forms.Textarea(attrs={
            'placeholder': 'Введите блюда и цены в формате: \nНазвание1 - Цена1\nНазвание2 - Цена2',
            'rows': 7,
            'cols': 30
        }),
        required=True
    )

    class Meta:
        model = Order
        fields = ['status', 'items']

    def __init__(self, *args, **kwargs):
        # Преобразуем JSON-список блюд в удобный текстовый формат для редактирования
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.items:
            items_formatted = "\n".join(
                f"{item['name']} - {item['price']}" for item in self.instance.items
            )
            self.fields['items'].initial = items_formatted

    def clean_items(self):
        items_raw = self.cleaned_data['items']
        items_list = []
        try:
            for line in items_raw.splitlines():
                name, price = line.split('-')
                items_list.append({'name': name.strip(), 'price': float(price.strip())})
        except ValueError:
            raise forms.ValidationError("Введите данные в формате: Название - Цена (каждая пара на новой строке)")

        if len(items_list) == 0:
            raise forms.ValidationError("Список блюд пуст. Добавьте хотя бы одно блюдо.")
        return items_list


    

