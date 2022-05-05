from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tattoo, Piercings
from django.core.paginator import Paginator


def tattoo(request):
    """Exibe todos os integrantes do Motoclube"""
    tattoo = Tattoo.objects.order_by('-data_inclusao')
    paginator = Paginator(tattoo, 24)
    page = request.GET.get('page')
    tattoo_por_pagina = paginator.get_page(page)

    dados = {
        'tattoo': tattoo_por_pagina
    }
    return render(request, 'produtos/tattoo.html', dados)


def cria_tattoo(request):
    """Cria integrante"""
    if request.method == 'POST':
        nome_tattoo = request.POST['nome_tattoo']
        foto_tattoo = request.FILES['foto_tattoo']
        data_inclusao = request.POST['data_inclusao']
        destaque = request.POST.get('destaque', False)

        if destaque == 'on':
            destaque = True
        else:
            destaque = False

        tattoo = Tattoo.objects.create(nome_tattoo=nome_tattoo,
                                       foto_tattoo=foto_tattoo,
                                       data_inclusao=data_inclusao,
                                       destaque=destaque)
        tattoo.save()
        return redirect('tattoo')
    else:
        return render(request, 'produtos/cria_tattoo.html')


def deleta_tattoo(request, id_tattoo):
    """Delete um album da base de dados"""
    tattoo = get_object_or_404(Tattoo, pk=id_tattoo)
    tattoo.delete()
    return redirect('tattoo')


def edita_tattoo(request, id_tattoo):
    """Edita o album selecionado"""
    tattoo = get_object_or_404(Tattoo, pk=id_tattoo)

    data = tattoo.data_inclusao
    tattoo.data_inclusao = datetime.strftime(data, '%Y-%m-%d')

    dados = {
        'tattoo': tattoo
    }
    return render(request, 'produtos/edita_tattoo.html', dados)


def atualiza_tattoo(request):
    if request.method == 'POST':
        id_tattoo = request.POST['tattoo.id']
        a = Tattoo.objects.get(pk=id_tattoo)
        a.nome_tattoo = request.POST['nome_tattoo']
        a.data_inclusao = request.POST['data_inclusao']
        a.destaque = request.POST.get('destaque', False)

        if 'foto_tattoo' in request.FILES:
            a.foto_tattoo = request.FILES['foto_tattoo']

        # Valida integrante ativo
        if a.destaque == 'on':
            a.destaque = True
        else:
            a.destaque = False

        a.save()
        return redirect('tattoo')


def piercings(request):
    """Exibe todos os integrantes do Motoclube"""
    piercings = Piercings.objects.order_by('-data_inclusao')
    paginator = Paginator(piercings, 24)
    page = request.GET.get('page')
    piercings_por_pagina = paginator.get_page(page)

    dados = {
        'piercings': piercings_por_pagina
    }
    return render(request, 'produtos/piercings.html', dados)


def cria_piercings(request):
    """Cria integrante"""
    if request.method == 'POST':
        nome_piercings = request.POST['nome_piercings']
        foto_piercings = request.FILES['foto_piercings']
        data_inclusao = request.POST['data_inclusao']
        destaque = request.POST.get('destaque', False)

        # Valida integrante ativo
        if destaque == 'on':
            destaque = True
        else:
            destaque = False

        piercings = Piercings.objects.create(nome_piercings=nome_piercings,
                                             foto_piercings=foto_piercings,
                                             data_inclusao=data_inclusao,
                                             destaque=destaque)
        piercings.save()
        return redirect('piercings')
    else:
        return render(request, 'produtos/cria_piercings.html')


def deleta_piercings(request, id_piercings):
    """Delete um piercings da base de dados"""
    piercings = get_object_or_404(Piercings, pk=id_piercings)
    piercings.delete()
    return redirect('piercings')


def edita_piercings(request, id_piercings):
    """Edita o piercings selecionado"""
    piercings = get_object_or_404(Piercings, pk=id_piercings)

    data = piercings.data_inclusao
    piercings.data_inclusao = datetime.strftime(data, '%Y-%m-%d')

    dados = {
        'piercings': piercings
    }
    return render(request, 'produtos/edita_piercings.html', dados)


def atualiza_piercings(request):
    if request.method == 'POST':
        id_piercings = request.POST['piercings.id']
        a = Piercings.objects.get(pk=id_piercings)
        a.nome_piercings = request.POST['nome_piercings']
        a.data_inclusao = request.POST['data_inclusao']
        a.destaque = request.POST.get('destaque', False)

        if 'foto_piercings' in request.FILES:
            a.foto_piercings = request.FILES['foto_piercings']

        # Valida integrante ativo
        if a.destaque == 'on':
            a.destaque = True
        else:
            a.destaque = False

        a.save()
        return redirect('piercings')
