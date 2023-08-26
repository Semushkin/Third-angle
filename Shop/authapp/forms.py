from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, SetPasswordForm
from authapp.models import User
from django import forms
from django.db import models


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',
                  'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['username'].widget.attrs['onkeydown'] = 'return /[a-zA-Z0-9_]/i.test(event.key)'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        # self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        # self.fields['last_name'].widget.attrs['onkeydown'] = 'return /[a-zA-Zа-яА-Я]/i.test(event.key)'
        # self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        # self.fields['first_name'].widget.attrs['onkeydown'] = 'return /[a-zA-Zа-яА-Я]/i.test(event.key)'
        # self.fields['gender'].widget.attrs['placeholder'] = 'Укажите пол'
        # self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        # self.fields['age'].widget.attrs['placeholder'] = 'Введите возраст'
        # self.fields['address'].widget.attrs['placeholder'] = 'Введите адрес'
        # self.fields['telephone'].widget.attrs['placeholder'] = '+7 (___) ___ - __ - __'
        # self.fields['telephone'].widget.attrs['value'] = '+7 (___) ___ - __ - __'
        # self.fields['telephone'].widget.attrs['mask'] = '+7 (___) ___ - __ - __'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'


class UserDataForm(forms.Form):

    NOT_SELECTED = '------'

    GENDER = {
        (NOT_SELECTED, '------'),
        ('М', 'М'),
        ('Ж', 'Ж')
    }

    DEFAULT = 'Customer'

    GROUP_USER = {
        (DEFAULT, 'Customer'),
        ('Seller', 'Seller'),
        ('Moderator', 'Moderator')
    }

    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.CharField(max_length=64)
    gender = forms.ChoiceField(choices=GENDER)
    in_group = forms.ChoiceField(choices=GROUP_USER)
    age = forms.IntegerField()
    address = forms.CharField(max_length=128)
    telephone = forms.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super(UserDataForm, self).__init__(*args, **kwargs)
        self.fields["in_group"].required = False

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'


class UserEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['username'].widget.attrs['onkeydown'] = 'return /[a-zA-Z0-9_]/i.test(event.key)'
        # self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        # self.fields['last_name'].widget.attrs['onkeydown'] = 'return /[a-zA-Zа-яА-Я]/i.test(event.key)'
        # self.fields['gender'].widget.attrs['placeholder'] = 'Укажите пол'
        # self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        # self.fields['first_name'].widget.attrs['onkeydown'] = 'return /[a-zA-Zа-яА-Я]/i.test(event.key)'
        # self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        # self.fields['age'].widget.attrs['placeholder'] = 'Введите возраст'
        # self.fields['address'].widget.attrs['placeholder'] = 'Введите адрес'
        # self.fields['telephone'].widget.attrs['placeholder'] = '+7 (___) ___ - __ - __'
        # self.fields['telephone'].widget.attrs['value'] = '+7 (___) ___ - __ - __'
        # self.fields['telephone'].widget.attrs['mask'] = '+7 (___) ___ - __ - __'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'


class SetNewPassword(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ('new_password1',
                  'new_password2')

    def __init__(self, *args, **kwargs):
        super(SetNewPassword, self).__init__(*args, **kwargs)

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'


# class UserDataCreateUpdateForm(forms.Form):
#
#     NOT_SELECTED = '------'
#
#     GENDER = {
#         (NOT_SELECTED, '------'),
#         ('М', 'М'),
#         ('Ж', 'Ж')
#     }
#
#     DEFAULT = '------'
#
#     GROUP_USER = {
#         (DEFAULT, 'Customer'),
#         ('Seller', 'Seller'),
#         ('Moderator', 'Moderator')
#     }
#
#     last_name = forms.CharField(max_length=64)
#     first_name = forms.CharField(max_length=64)
#     email = forms.CharField(max_length=64)
#     gender = forms.ChoiceField(choices=GENDER)
#     in_group = forms.ChoiceField(choices=GROUP_USER)
#     age = forms.IntegerField(min_value=0)
#     address = forms.CharField(max_length=100)
#     telephone = forms.CharField(max_length=30)
#
#     def __init__(self, *args, **kwargs):
#         super(UserDataCreateUpdateForm, self).__init__(*args, **kwargs)
#         self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
#         self.fields['last_name'].widget.attrs['onkeydown'] = 'return /[a-zA-Zа-яА-Я]/i.test(event.key)'
#         self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
#         self.fields['first_name'].widget.attrs['onkeydown'] = 'return /[a-zA-Zа-яА-Я]/i.test(event.key)'
#         self.fields['gender'].widget.attrs['placeholder'] = 'Укажите пол'
#         self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
#         self.fields['age'].widget.attrs['placeholder'] = 'Введите возраст'
#         self.fields['address'].widget.attrs['placeholder'] = 'Введите адрес'
#         self.fields['telephone'].widget.attrs['placeholder'] = '+7 (___) ___ - __ - __'
#         self.fields['telephone'].widget.attrs['value'] = '+7 (___) ___ - __ - __'
#         self.fields['telephone'].widget.attrs['mask'] = '+7 (___) ___ - __ - __'
#
#         for filed_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'u-full-width'
