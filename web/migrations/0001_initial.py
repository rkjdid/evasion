# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 12:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default=b'', max_length=60, verbose_name=b'Mail')),
                ('firstname', models.CharField(max_length=60, verbose_name=b'First Name')),
                ('lastname', models.CharField(blank=True, max_length=60, null=True, verbose_name=b'Name')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'Phone')),
                ('date_reservation', models.DateField(verbose_name=b'Reservation Date')),
                ('date_filled', models.BooleanField(default=False, verbose_name=b'Reservation Date filled')),
                ('message', models.TextField(blank=True, null=True, verbose_name=b'Message')),
                ('message_sent', models.BooleanField(default=False, verbose_name=b'Message sent')),
                ('date_message', models.DateTimeField(default=datetime.datetime(2017, 2, 8, 12, 27, 56, 633653, tzinfo=utc), verbose_name=b'Message Date')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Referer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=120, unique=True, verbose_name=b'Host name')),
                ('hits', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['host'],
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=255, unique=True, verbose_name=b'IP')),
                ('hits', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='VisitorReferer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('referer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Referer')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Visitor')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='visitor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='web.Visitor'),
        ),
    ]
