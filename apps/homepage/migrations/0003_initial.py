# Generated by Django 4.0.2 on 2022-05-09 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0002_delete_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(blank=True, upload_to='fotos/%m/%Y/')),
                ('banner_ativo', models.BooleanField(default=False)),
            ],
        ),
    ]
