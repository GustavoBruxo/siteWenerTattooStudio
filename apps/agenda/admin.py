from django.contrib import admin
from .models import Agenda


class ListandoAgendas(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data_agenda', 'hora_inicio', 'hora_fim', 'confirmacao',)
    list_display_links = ('id', 'usuario', 'data_agenda', 'hora_inicio', 'hora_fim',)
    search_fields = ('data_agenda',)
    list_editable = ('confirmacao',)
    list_per_page = 10


admin.site.register(Agenda, ListandoAgendas)
