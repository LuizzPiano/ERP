# Generated by Django 4.2 on 2023-04-28 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=30)),
                ('disponivel', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('nome', 'rua', 'numero')},
            },
        ),
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ind', models.CharField(max_length=50)),
                ('data_admissao', models.DateField()),
                ('disponivel', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Colaboradores',
                'verbose_name_plural': 'Colaboradores',
            },
        ),
        migrations.CreateModel(
            name='Folga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_folga', models.DateField()),
                ('colaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escalas.colaboradores')),
            ],
            options={
                'unique_together': {('data_folga', 'colaborador')},
            },
        ),
        migrations.CreateModel(
            name='Escala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(null=True)),
                ('disponivel', models.BooleanField(default=True)),
                ('base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escalas.base')),
                ('colaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escalas.colaboradores')),
            ],
            options={
                'unique_together': {('colaborador', 'data')},
            },
        ),
    ]
