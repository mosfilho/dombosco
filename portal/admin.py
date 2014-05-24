from django.contrib import admin
from models import *
from forms import *
from fullcalendar.admin import CalendarEventAdminInline
from . import aplicar_tags, aplicar_layout
from datetime import datetime

class TabelaLayoutAdmin(admin.ModelAdmin):
    model = TabelaLayout
    ordering = ('id',)
    list_display = ('id','local',)

class ImagemGaleriaAdminInline(admin.StackedInline):
    model = ImagemGaleria
    search_fields = ('galeria',)

class GaleriaAdmin(admin.ModelAdmin):
    model = Galeria
    form = GaleriaForm
    inlines = [ImagemGaleriaAdminInline]
    list_display = ('id','nome',)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        obj.data_criacao = datetime.now()

        super(GaleriaAdmin, self).save_model(request, obj, form, change)

        aplicar_tags(obj, form.cleaned_data['tags'])
        aplicar_layout(obj, form.cleaned_data['layout'], form.cleaned_data['data_expiracao'])

class GaleriaAdminInline(admin.StackedInline):
    model = Galeria
    inlines = [ImagemGaleriaAdminInline]
    extra = 1

class GaleriaAdminInline(admin.StackedInline):
    model = Galeria
    inlines = [ImagemGaleriaAdminInline]
    extra = 1

class PublicacaoAdmin(admin.ModelAdmin):
    model = Publicacao
    form = PublicacaoForm
    list_display = ('nome','data_criacao','autor','tipo_publicacao','esta_ativo','id','numeroVisitas',)

    def save_model(self, request, obj, form, change):
        if not Publicacao.objects.filter(id = obj.id).exists():
            obj.autor = request.user
            obj.data_criacao = datetime.now()

        obj.save()

        aplicar_tags(obj, form.cleaned_data['tags'])
        aplicar_layout(obj, form.cleaned_data['layout'], form.cleaned_data['data_expiracao'])

class PublicacaoAdminInline(admin.StackedInline):
    model = Publicacao
    extra = 1

class AgregadorAdmin(admin.ModelAdmin):
    model = Agregador
    inlines = [PublicacaoAdminInline, GaleriaAdminInline, CalendarEventAdminInline]

class LayoutAdmin(admin.ModelAdmin):
    model = Layout
    list_display = ('local','content_type','object_id','data_expiracao',)

# Register your models here.
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Agregador, AgregadorAdmin)
admin.site.register(TipoPublicacao)
admin.site.register(TabelaLayout, TabelaLayoutAdmin)
admin.site.register(Tag)
admin.site.register(Layout, LayoutAdmin)
