# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('strategy', '0001_initial'),
        ('symbols', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tradeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tradingTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('waitingtime', models.IntegerField()),
                ('trade_config_json', models.TextField(blank=True, null=True)),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.strategies')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symbols.symbols')),
            ],
        ),
        migrations.AddField(
            model_name='tradelog',
            name='trade_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.tradingTask'),
        ),
    ]
