# Generated by Django 2.1.1 on 2018-11-21 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('is', '0004_auto_20181121_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firma',
            name='eposta',
        ),
    ]