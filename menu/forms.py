# -*- encoding: utf-8 -*-

from django import forms
from models import Menu
from redactor.widgets import RedactorEditor
from django.contrib.admin import widgets

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        widgets = {'content' : RedactorEditor()}
