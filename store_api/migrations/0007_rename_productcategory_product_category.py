# Generated by Django 3.2.6 on 2021-08-12 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0006_productcategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductCategory',
            new_name='Product_Category',
        ),
    ]