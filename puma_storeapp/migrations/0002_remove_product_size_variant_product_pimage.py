# Generated by Django 5.0 on 2023-12-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puma_storeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size_Variant',
        ),
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
    ]