# Generated by Django 3.2.6 on 2021-08-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0002_auto_20210812_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='test',
            field=models.ManyToManyField(to='store_api.Category'),
        ),
    ]