from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from datetime import datetime
from .models import Agenda



def agenda(request):
    """ Função para retonar as agendas cadastrasdas """
    agendamento = Agenda.objects.filter(confirmacao=True, data_agenda__gte=datetime.now())

    dados = {
        'agendamentos': agendamento
    }

    return render(request, 'agenda/agenda.html', dados)


def criar_agenda(request):
    """ Função criar um agendamento """
    if request.method == 'POST':
        usuario = get_object_or_404(User, pk=request.user.id)
        data_agenda = datetime.strptime(request.POST['data_agenda'], '%Y-%m-%d')
        hora_inicio = datetime.strptime(request.POST['hora_inicio'], '%H:%M')
        hora_fim = datetime.strptime(request.POST['hora_fim'], '%H:%M')

        if Agenda.objects.filter(data_agenda=data_agenda,
                                 hora_inicio=hora_inicio,
                                 hora_fim=hora_fim,
                                 confirmacao=True).exists():
            messages.error(request, 'Horário já reservado.')
            return redirect('criar_agenda')
        
        if data_agenda < datetime.now():
            messages.error(request, 'Data inferior a data atual.')
            return redirect('criar_agenda')

        agenda = Agenda.objects.create(usuario=usuario,
                                       data_agenda=data_agenda,
                                       hora_inicio=hora_inicio,
                                       hora_fim=hora_fim)
        agenda.save()

        return redirect('agenda')
    else:
        return render(request, 'agenda/criar_agenda.html')
