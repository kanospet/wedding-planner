# Generated by Django 3.1 on 2020-08-30 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200830_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorialseries',
            old_name='turorial_category',
            new_name='tutorial_category',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 30, 22, 22, 33, 662126), verbose_name='date published'),
        ),
    ]
