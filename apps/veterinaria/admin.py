from django.contrib import admin
from apps.veterinaria.models import Cliente, HistoriaClinica, Mascota, TipoMascota

# Register your models here.

admin.site.register(Cliente)
admin.site.register(TipoMascota)

class HistoriaClinica_Inline(admin.StackedInline):
    model = HistoriaClinica
    extra = 0

class Mascota_Admin(admin.ModelAdmin):
    inlines = [
        HistoriaClinica_Inline,
    ]

admin.site.register(Mascota, Mascota_Admin)


