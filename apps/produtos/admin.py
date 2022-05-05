from django.contrib import admin
from .models import Tattoo, Piercings

# Register your models here.


class ListandoTattoo(admin.ModelAdmin):
    list_display = ('id', 'nome_tattoo', 'data_inclusao',
                    'destaque')
    list_display_links = ('id', 'nome_tattoo')
    list_editable = ('destaque', )
    list_per_page = 20


admin.site.register(Tattoo, ListandoTattoo)


class ListandoPiercings(admin.ModelAdmin):
    list_display = ('id', 'nome_piercings', 'data_inclusao',
                    'destaque')
    list_display_links = ('id', 'nome_piercings')
    list_editable = ('destaque', )
    list_per_page = 20


admin.site.register(Piercings, ListandoPiercings)
