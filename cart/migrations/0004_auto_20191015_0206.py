# Generated by Django 2.2.5 on 2019-10-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_product_imagesrc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='prodcut_name',
        ),
        migrations.AddField(
            model_name='product',
            name='imagesrc',
            field=models.CharField(default='Null', max_length=500),
        ),
    ]