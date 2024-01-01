# Generated by Django 5.0 on 2023-12-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puma_storeapp', '0004_cart_store_delete_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart_store',
            old_name='pid',
            new_name='Pid',
        ),
        migrations.AddField(
            model_name='cart_store',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart_store',
            name='product_qty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]