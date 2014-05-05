from django.contrib import admin
from models import *
from forms import *
from fullcalendar.admin import CalendarEventAdminInline

class ImagemGaleriaAdminInline(admin.StackedInline):
    model = ImagemGaleria
    search_fields = ('galeria',)

class GaleriaAdmin(admin.ModelAdmin):
    model = Galeria
    form = GaleriaForm
    inlines = [ImagemGaleriaAdminInline]
    list_display = ('id','nome',)

class GaleriaAdminInline(admin.StackedInline):
    model = Galeria
    inlines = [ImagemGaleriaAdminInline]
    extra = 1

class PublicacaoAdmin(admin.ModelAdmin):
    model = Publicacao
    form = PublicacaoForm

class PublicacaoAdminInline(admin.StackedInline):
    model = Publicacao
    form = PublicacaoForm
    extra = 1

class AgregadorAdmin(admin.ModelAdmin):
    model = Agregador
    inlines = [PublicacaoAdminInline, GaleriaAdminInline, CalendarEventAdminInline]

# Register your models here.
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Agregador, AgregadorAdmin)
admin.site.register(TipoPublicacao)
admin.site.register(TabelaLocal)
