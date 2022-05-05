document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        timeZone: 'America/Sao_Paulo',
        themeSystem: 'bootstrap5',
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        headerToolbar: {
            center: 'dayGridMonth,timeGridWeek'
        },
        views: {
            dayGridMonth: {
                titleFormat: { year: 'numeric', month: '2-digit', day: '2-digit' }
            }
        },
        events: [
        {% for agendamento in agendamentos %}
            {
                title: "{{agendamento.usuario}}",
                start: "{{agendamento.data_agenda | date:'Y-m-d'}}" + 'T' + "{{agendamento.hora_inicio}}",
                end: "{{agendamento.data_agenda | date:'Y-m-d'}}" + 'T' + "{{agendamento.hora_fim}}"
            },
            {% endfor %}
        ],
        eventTimeFormat: {
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        }
    });
    calendar.setOption('locale', 'pt-br');
    calendar.render();
});