# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-14 20:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('books', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('issued_book', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
    ]
