# Generated by Django 4.2.2 on 2023-07-04 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_alter_products_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('size', models.CharField(blank=True, max_length=20)),
                ('colour', models.CharField(blank=True, max_length=20)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='products.cart')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.products')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]