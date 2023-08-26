from django import forms
from basketapp.models import Request, Order


class RequestCreateForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = (
            'text',
            'status',
            'user',
        )

    def __init__(self, *args, **kwargs):
        super(RequestCreateForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = 'Введите текст'
        self.fields['text'].widget.attrs['class'] = 'u-full-width'


class RequestUpdateForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = (
            'status',
        )

    def __init__(self, *args, **kwargs):
        super(RequestUpdateForm, self).__init__(*args, **kwargs)


class OrderStatusChangeForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'status',
        )

    def __init__(self, *args, **kwargs):
        super(OrderStatusChangeForm, self).__init__(*args, **kwargs)
