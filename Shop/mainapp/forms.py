from django import forms
from mainapp.models import Book


class BoorCreateUpdateForm(forms.ModelForm):
    foto = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Book
        fields = (
            'name',
            'author',
            'foto',
            'article',
            'date_receipt',
            'category',
            'description',
            'price',
        )

    def __init__(self, *args, **kwargs):
        super(BoorCreateUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название'
        self.fields['author'].widget.attrs['placeholder'] = 'Укажите автора'
        self.fields['article'].widget.attrs['placeholder'] = 'Укажите артикул'
        self.fields['category'].widget.attrs['placeholder'] = 'Выберете жанр'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание'

        self.fields['date_receipt'] = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'