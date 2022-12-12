from django import forms
from portafoliopersonal.models import Portafolio



class PortafioForm(forms.ModelForm):
    class Meta:
        model = Portafolio
        fields = ['foto','project_name', 'description', 'tags','github']
