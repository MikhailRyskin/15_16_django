# Generated by Django 3.2.6 on 2021-08-31 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, default=0, verbose_name='цена'),
        ),
    ]
