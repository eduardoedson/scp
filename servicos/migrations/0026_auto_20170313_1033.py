# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0025_auto_20170225_1935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chamado',
            options={'verbose_name': 'Chamado', 'verbose_name_plural': 'Chamados'},
        ),
    ]
