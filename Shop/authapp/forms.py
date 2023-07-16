from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from authapp.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',
                  'password1',
                  'password2',
                  'last_name',
                  'first_name',
                  'email',
                  'age',
                  'address',
                  'telephone')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
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
        self.fields['password'].widget.attrs['password'] = 'Введите пароль'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'u-full-width'