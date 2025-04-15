from django import forms
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
        min_length=6,
        error_messages={'min_length': "Пароль должен содержать не менее 6 символов."}
    )
    confirm_password = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'})
    )

    class Meta:
        model = User
        fields = ['login', 'full_name', 'phone', 'email']
        widgets = {
            'login': forms.TextInput(attrs={'placeholder': 'Введите логин'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Введите ФИО'}),
            'phone': forms.TextInput(attrs={'placeholder': '+7(XXX)-XXX-XX-XX'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Пароли не совпадают.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password1']