# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uName', models.CharField(max_length=20)),
                ('uPasswd', models.CharField(max_length=20)),
                ('uEmail', models.CharField(max_length=30)),
                ('uShou', models.CharField(default=b'', max_length=50)),
                ('uAddr', models.CharField(default=b'', max_length=50)),
                ('uTel', models.CharField(default=b'', max_length=20)),
                ('uYoubian', models.CharField(default=b'', max_length=6)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
