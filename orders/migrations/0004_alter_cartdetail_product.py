# Generated by Django 4.2 on 2024-03-06 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_review_created_at_review_create_at'),
        ('orders', '0003_alter_cartdetail_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='Product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_product', to='products.product'),
        ),
    ]