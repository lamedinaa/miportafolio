# Generated by Django 3.2.9 on 2022-01-09 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='problema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_problema', models.CharField(max_length=2)),
                ('nombre_problema', models.CharField(max_length=100)),
                ('plataforma_problema', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='solucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_solucion', models.TextField()),
                ('link_gist', models.CharField(max_length=100)),
                ('problema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milaboratorio.problema')),
            ],
        ),
    ]
