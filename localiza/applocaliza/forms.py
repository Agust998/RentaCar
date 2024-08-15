from django import forms 


class registroFormulario(forms.Form) :
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

class buscarAuto(forms.Form) :
    auto = forms.CharField()
    