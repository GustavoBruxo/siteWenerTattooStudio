# Generated by Django 4.0.2 on 2022-05-09 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_agenda_data_agenda_alter_agenda_hora_fim_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenda',
            options={'get_latest_by': 'order_date', 'verbose_name': 'agenda', 'verbose_name_plural': 'agendas'},
        ),
        migrations.AlterModelTable(
            name='agenda',
            table='agenda',
        ),
    ]
