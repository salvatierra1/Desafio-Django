from django import forms

from apps.veterinaria.models import Cliente



class ClienteForm(forms.ModelForm):
    
    class Meta:
        model= Cliente

        # Todos los campos
        fields = '__all__'
        
    
