# Generated by Django 3.2.6 on 2021-08-12 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0008_rename_product_category_productcategories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductCategories',
        ),
    ]
