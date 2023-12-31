# Generated by Django 4.2.2 on 2023-07-04 06:10

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='product_name', unique=True),
        ),
    ]
