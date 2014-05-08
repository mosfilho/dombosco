# -*- encoding: utf-8 -*-

from django import forms
from models import Publicacao, Galeria, TabelaLocal
from redactor.widgets import RedactorEditor
<<<<<<< HEAD
from . import tags_para_objeto
=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        widgets = {'texto' : RedactorEditor()}
    
    local_publicacao = forms.ModelChoiceField(queryset=TabelaLocal.objects.all(), required = False)
<<<<<<< HEAD
    tags = forms.CharField(max_length = 50, required = False, help_text = u'Separe as tags com vírgula.')

    def __init__(self, *args, **kwargs):
        super(PublicacaoForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['tags'].initial = tags_para_objeto(self.instance)
=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
    
    local_publicacao = forms.ModelChoiceField(queryset=TabelaLocal.objects.all(), required = False)
<<<<<<< HEAD
    tags = forms.CharField(max_length = 50, required = False, help_text = u'Separe as tags com vírgula.')

    def __init__(self, *args, **kwargs):
        super(GaleriaForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['tags'].initial = tags_para_objeto(self.instance)
=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
