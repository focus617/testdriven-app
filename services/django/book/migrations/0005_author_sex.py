# Generated by Django 2.1.3 on 2018-12-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20181204_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='sex',
            field=models.BooleanField(choices=[(0, '男'), (1, '女')], default=0, max_length=1),
        ),
    ]