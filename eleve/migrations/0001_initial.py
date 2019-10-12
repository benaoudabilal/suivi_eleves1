# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-10-11 19:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sortie', models.DateField(default='0')),
                ('date_entree', models.DateField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=20)),
                ('classe', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='eleve.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='Instructeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat', models.CharField(default=0, max_length=20)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Motif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motif_abs', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test1', models.IntegerField(default=0)),
                ('test2', models.IntegerField(default=0)),
                ('examen', models.IntegerField(default=0)),
                ('moyenne', models.IntegerField(default=0)),
                ('mention', models.CharField(default=0, max_length=20)),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleve.Eleve')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleve.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='instructeur',
            name='module',
            field=models.ManyToManyField(to='eleve.Module'),
        ),
        migrations.AddField(
            model_name='classe',
            name='specialities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleve.Specialities'),
        ),
        migrations.AddField(
            model_name='absence',
            name='eleve',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='eleve.Eleve'),
        ),
        migrations.AddField(
            model_name='absence',
            name='motif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleve.Motif'),
        ),
    ]