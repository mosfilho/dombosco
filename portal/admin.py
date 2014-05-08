from django.contrib import admin
from models import *
from forms import *
from fullcalendar.admin import CalendarEventAdminInline
<<<<<<< HEAD
<<<<<<< HEAD
from . import aplicar_tags, tags_para_objeto
=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0

class ImagemGaleriaAdminInline(admin.StackedInline):
    model = ImagemGaleria
    search_fields = ('galeria',)

class GaleriaAdmin(admin.ModelAdmin):
    model = Galeria
    form = GaleriaForm
    inlines = [ImagemGaleriaAdminInline]
    list_display = ('id','nome',)

<<<<<<< HEAD
<<<<<<< HEAD
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

=======
class GaleriaAdminInline(admin.StackedInline):
    model = Galeria
    inlines = [ImagemGaleriaAdminInline]
    extra = 1

>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
=======
class GaleriaAdminInline(admin.StackedInline):
    model = Galeria
    inlines = [ImagemGaleriaAdminInline]
    extra = 1

>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
class PublicacaoAdmin(admin.ModelAdmin):
    model = Publicacao
    form = PublicacaoForm

<<<<<<< HEAD
<<<<<<< HEAD
    def save_model(self, request, obj, form, change):
        super(PublicacaoAdmin, self).save_model(request, obj, form, change)

        aplicar_tags(obj, form.cleaned_data['tags'])

=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
class PublicacaoAdminInline(admin.StackedInline):
    model = Publicacao
    form = PublicacaoForm
    extra = 1

<<<<<<< HEAD
<<<<<<< HEAD
    def save_model(self, request, obj, form, change):
        super(PublicacaoAdminInline, self).save_model(request, obj, form, change)

        aplicar_tags(obj, form.cleaned_data['tags'])


=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
class AgregadorAdmin(admin.ModelAdmin):
    model = Agregador
    inlines = [PublicacaoAdminInline, GaleriaAdminInline, CalendarEventAdminInline]

# Register your models here.
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Agregador, AgregadorAdmin)
admin.site.register(TipoPublicacao)
admin.site.register(TabelaLocal)
<<<<<<< HEAD
<<<<<<< HEAD
admin.site.register(Tag)
=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
=======
>>>>>>> f158ccbe2cdc71801e30816132356c06033177d0
