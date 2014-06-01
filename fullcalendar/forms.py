# -*- encoding: utf-8 -*-
from django import forms
from models import CalendarEvent
from redactor.widgets import RedactorEditor

class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        widgets = {'text' : RedactorEditor()}

    def save(self, commit=True):
        instance = super(CalendarEventForm, self).save(commit=False)
        instance.url = instance.get_absolute_url()
        if commit:
            instance.save()
        return instance
