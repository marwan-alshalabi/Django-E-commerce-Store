# Generated by Django 4.2 on 2024-02-11 01:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_reviews_review_review_alter_product_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='created_at',
        ),
        migrations.AddField(
            model_name='review',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
