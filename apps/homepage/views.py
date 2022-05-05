from django.shortcuts import render
from .models import Banner
from produtos.models import Tattoo, Piercings
from django.core.paginator import Paginator


def index(request):
    """Renderiza a pagina inicial"""
    banner = Banner.objects.filter(banner_ativo=True)
    tattoo = Tattoo.objects.filter(destaque=True)
    piercing = Piercings.objects.filter(destaque=True)
    destaques = tattoo.union(piercing).order_by('-data_inclusao')
    paginator = Paginator(destaques, 9)
    page = request.GET.get('page')
    destaques_por_pagina = paginator.get_page(page)

    dados = {
        'banner': banner,
        'destaques': destaques_por_pagina
    }

    return render(request, 'wenertattoo/index.html', dados)


def cadastros(request):
    return render(request, 'wenertattoo/cadastros.html')


def agenda(request):
    return render(request, 'agenda/agenda.html')
