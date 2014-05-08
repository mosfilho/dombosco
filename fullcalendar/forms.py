# -*- encoding: utf-8 -*-
from django import forms
from models import CalendarEvent
from redactor.widgets import RedactorEditor

class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        widgets = {'text' : RedactorEditor()}

