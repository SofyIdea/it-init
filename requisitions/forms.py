from django import forms
from .models import Requests, Services

class RequestForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=Services.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="---------"
    )

    class Meta:
        model = Requests
        fields = ['email', 'phone', 'service', 'other_service_description', 'payment_method']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Введите email', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '+7(XXX)-XXX-XX-XX', 'class': 'form-control'}),
            'other_service_description': forms.Textarea(attrs={'placeholder': 'Опишите другую услугу...', 'rows': 3, 'class': 'form-control'}),
            'payment_method': forms.Select(choices=Requests.PAYMENT_METHOD_CHOICES, attrs={'class': 'form-control'}),
        }
        labels = {
            'email': 'Email',
            'phone': 'Телефон',
            'service': 'Выберите услугу',
            'other_service_description': 'Описание услуги',
            'payment_method': 'Способ оплаты',
        }

    def clean(self):
        cleaned_data = super().clean()
        service = cleaned_data.get('service')
        other_service_description = cleaned_data.get('other_service_description')

        if service and service.id == 7 and not other_service_description:
            raise forms.ValidationError("Пожалуйста, опишите прочие услуги.")

        return cleaned_data