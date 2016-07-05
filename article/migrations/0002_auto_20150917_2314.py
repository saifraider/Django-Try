# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import article.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=datetime.datetime(2015, 9, 17, 17, 44, 20, 28000, tzinfo=utc), upload_to=article.models.get_upload_file_name),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
