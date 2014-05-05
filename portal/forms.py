# -*- encoding: utf-8 -*-

from django import forms
from models import Publicacao, Galeria, TabelaLocal
from redactor.widgets import RedactorEditor

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        widgets = {'texto' : RedactorEditor()}
    
    local_publicacao = forms.ModelChoiceField(queryset=TabelaLocal.objects.all(), required = False)

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
    
    local_publicacao = forms.ModelChoiceField(queryset=TabelaLocal.objects.all(), required = False)
