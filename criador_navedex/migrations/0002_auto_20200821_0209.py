# Generated by Django 3.1 on 2020-08-21 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criador_navedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='naver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projetos', to='criador_navedex.naver'),
        ),
    ]
