# Generated by Django 5.0 on 2023-12-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puma_storeapp', '0008_store_created_at_store_product_qty_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='product_qty',
        ),
        migrations.AddField(
            model_name='store',
            name='qty',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
