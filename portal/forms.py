# -*- encoding: utf-8 -*-

from django import forms
from models import Publicacao, Galeria, TabelaLayout
from redactor.widgets import RedactorEditor
from fullcalendar.models import CalendarEvent
from . import tags_para_objeto, layout_para_objeto
from django.contrib.admin import widgets

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        widgets = {'texto' : RedactorEditor()}
    
    layout = forms.ModelChoiceField(queryset=TabelaLayout.objects.all(), label = 'Layout', required = False)
    data_expiracao = forms.DateTimeField(required = False, widget=widgets.AdminSplitDateTime())
    tags = forms.CharField(max_length = 50, required = False, help_text = u'Separe as tags com vírgula.')

    def __init__(self, *args, **kwargs):
        super(PublicacaoForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['tags'].initial = tags_para_objeto(self.instance)
            self.fields['layout'].initial = layout_para_objeto(self.instance)

    def clean_layout(self):
        if self.cleaned_data['layout']:
            local = TabelaLayout.objects.get(local = self.cleaned_data['layout'])
            if local.tem_imagem and not self.cleaned_data['imagem_apresentacao']:
                raise forms.ValidationError('Necessita imagem para este tipo de layout')
            return self.cleaned_data['layout']


class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
    
    layout = forms.ModelChoiceField(queryset=TabelaLayout.objects.all(), label = 'Layout', required = False)
    data_expiracao = forms.DateTimeField(required = False, widget=widgets.AdminSplitDateTime())
    tags = forms.CharField(max_length = 50, required = False, help_text = u'Separe as tags com vírgula.')

    def __init__(self, *args, **kwargs):
        super(GaleriaForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['tags'].initial = tags_para_objeto(self.instance)
            self.fields['layout'].initial = layout_para_objeto(self.instance)
