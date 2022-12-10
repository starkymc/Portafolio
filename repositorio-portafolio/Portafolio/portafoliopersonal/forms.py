from django import forms
from portafoliopersonal.models import Portafolio

class LoginForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class PortafioForm(forms.ModelForm):
    class Meta:
        model = Portafolio
        fields = ('__all__')