# Generated by Django 3.2.9 on 2022-01-09 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('milaboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solucion',
            name='problema',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='milaboratorio.problema'),
        ),
    ]
