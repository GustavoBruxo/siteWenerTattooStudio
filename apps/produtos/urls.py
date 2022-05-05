from django.urls import path
from .views import *

urlpatterns = [
    path('tattoo/', tattoo, name='tattoo'),
    path('tattoo/cria/tattoo', cria_tattoo, name='cria_tattoo'),
    path('tattoo/edita/<int:id_tattoo>', edita_tattoo, name='edita_tattoo'),
    path('tattoo/deleta/<int:id_tattoo>', deleta_tattoo, name='deleta_tattoo'),
    path('tattoo/atualiza_tattoo', atualiza_tattoo, name='atualiza_tattoo'),
    path('piercings/', piercings, name='piercings'),
    path('piercings/cria/piercings', cria_piercings, name='cria_piercings'),
    path('piercings/edita/<int:id_piercings>', edita_piercings, name='edita_piercings'),
    path('piercings/deleta/<int:id_piercings>', deleta_piercings, name='deleta_piercings'),
    path('piercings/atualiza_piercings', atualiza_piercings, name='atualiza_piercings')
]
