from django import forms
from django.contrib.auth.models import User
from contact.models import Contacto

class ContactModelFormCreate(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'nombre',
            'email',
            'comentario'
        ]
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "prueba" in email:
            raise forms.ValidationError("El email no parece ser correcto")
        return email
