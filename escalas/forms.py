from django.forms import ModelForm
from .models import (
    Colaboradores,
    Base,
    Folga,
    Escala
)


class ColaboradoresForm(ModelForm):
    class Meta:
        model = Colaboradores
        fields = '__all__'


class BaseForm(ModelForm):
    class Meta:
        model = Base
        fields = '__all__'


class FolgaForm(ModelForm):
    class Meta:
        model = Folga
        fields = '__all__'
    

class EscalaForm(ModelForm):
    class Meta:
        model = Escala
        fields = '__all__'
