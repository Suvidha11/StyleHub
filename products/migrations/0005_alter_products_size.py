# Generated by Django 4.2.2 on 2023-07-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.ManyToManyField(to='products.size_varient'),
        ),
    ]
