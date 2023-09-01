from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class RegistrationForm(UserCreationForm):

    username = forms.CharField(
        label='Логин',
        help_text='<span class="help-text"><br> - Должен быть уникальным</span>',
    )

    email = forms.EmailField(
        
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'placeholder': 'user@gmail.com'})
    )

    password1 = forms.CharField(
        label='Пароль',
        
        widget=forms.PasswordInput(),
        help_text='<span class="help-text"><br> - Минимальная длина пароля: 8 символов <br> - Пароль не может содержать только цифры</span>',
    )

    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(),
        help_text='<span class="help-text"></span>',
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует.')
        return email

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].label = 'Логин'
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })