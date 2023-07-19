from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, SetPasswordForm
from authapp.models import User
from django import forms


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',
                  'password1',
                  'password2',
                  'last_name',
                  'first_name',
                  'gender',
                  'email',
                  'age',
                  'address',
                  'telephone')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['username'].widget.attrs['onkeydown'] = 'return /[a-zA-Z0-9_]/i.test(event.key)'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['last_name'].widget.attrs['onkeydown'] = 'return /[a-zA-Zа-яА-Я]/i.test(event.key)'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['first_name'].widget.attrs['onkeydown'] = 'return /[a-zA-Zа-яА-Я]/i.test(event.key)'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['age'].widget.attrs['placeholder'] = 'Введите возраст'
        self.fields['address'].widget.attrs['placeholder'] = 'Введите адрес'
        self.fields['telephone'].widget.attrs['placeholder'] = 'Введите телефон'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'


class UserEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',
                  'last_name',
                  'gender',
                  'first_name',
                  'email',
                  'age',
                  'address',
                  'telephone',)

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['gender'].widget.attrs['placeholder'] = 'Укажите пол'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['age'].widget.attrs['placeholder'] = 'Введите возраст'
        self.fields['address'].widget.attrs['placeholder'] = 'Введите адрес'
        self.fields['telephone'].widget.attrs['placeholder'] = 'Введите телефон'

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
