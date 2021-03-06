# Generated by Django 4.0.2 on 2022-05-09 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0003_delete_piercings_delete_tattoo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piercings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_piercings', models.CharField(max_length=100)),
                ('foto_piercings', models.ImageField(blank=True, upload_to='fotos/%m/%Y/')),
                ('data_inclusao', models.DateTimeField()),
                ('destaque', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tattoo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tattoo', models.CharField(max_length=100)),
                ('foto_tattoo', models.ImageField(blank=True, upload_to='fotos/%m/%Y/')),
                ('data_inclusao', models.DateTimeField()),
                ('destaque', models.BooleanField(default=True)),
            ],
        ),
    ]
