# Generated by Django 2.1.1 on 2018-11-29 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0006_auto_20181129_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firma',
            name='kategori',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='system.Kategori', verbose_name='Kategori'),
        ),
    ]