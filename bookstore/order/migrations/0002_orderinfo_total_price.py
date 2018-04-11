# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='total_price',
            field=models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总价', default=0),
        ),
    ]
