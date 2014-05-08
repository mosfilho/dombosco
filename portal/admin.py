from django.contrib import admin
from models import *
from forms import *
from fullcalendar.admin import CalendarEventAdminInline
from . import aplicar_tags, tags_para_objeto

class ImagemGaleriaAdminInline(admin.StackedInline):
    model = ImagemGaleria
    search_fields = ('galeria',)

class GaleriaAdmin(admin.ModelAdmin):
    model = Galeria
    form = GaleriaForm
    inlines = [ImagemGaleriaAdminInline]
    list_display = ('id','nome',)

    def save_model(self, request, obj, form, change):
        super(GaleriaAdmin, self).save_model(request, obj, form, change)

        aplicar_tags(obj, form.cleaned_data['tags'])

class GaleriaAdminInline(admin.StackedInline):
    model = Galeria
    form = GaleriaForm
    inlines = [ImagemGaleriaAdminInline]
    extra = 1

    def save_model(self, request, obj, form, change):
        super(GaleriaAdminInline, self).save_model(request, obj, form, change)

        aplicar_tags(obj, form.cleaned_data['tags'])

class PublicacaoAdmin(admin.ModelAdmin):
    model = Publicacao
    form = PublicacaoForm

    def save_model(self, request, obj, form, change):
        super(PublicacaoAdmin, self).save_model(request, obj, form, change)

        aplicar_tags(obj, form.cleaned_data['tags'])

class PublicacaoAdminInline(admin.StackedInline):
    model = Publicacao
    form = PublicacaoForm
    extra = 1

    def save_model(self, request, obj, form, change):
        super(PublicacaoAdminInline, self).save_model(request, obj, form, change)

        aplicar_tags(obj, form.cleaned_data['tags'])


class AgregadorAdmin(admin.ModelAdmin):
    model = Agregador
    inlines = [PublicacaoAdminInline, GaleriaAdminInline, CalendarEventAdminInline]

# Register your models here.
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Agregador, AgregadorAdmin)
admin.site.register(TipoPublicacao)
admin.site.register(TabelaLocal)
admin.site.register(Tag)
