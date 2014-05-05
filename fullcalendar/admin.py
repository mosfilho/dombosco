from django.contrib import admin
from .models import CalendarEvent
from .forms import CalendarEventForm

class CalendarEventAdminInline(admin.StackedInline):
    model = CalendarEvent
    form = CalendarEventForm

class CalendarEventAdmin(admin.ModelAdmin):
    model = CalendarEvent
    form = CalendarEventForm

admin.site.register(CalendarEvent, CalendarEventAdmin)
