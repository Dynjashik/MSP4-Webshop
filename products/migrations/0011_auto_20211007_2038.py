# Generated by Django 3.2.7 on 2021-10-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, default='', max_length=254),
            preserve_default=False,
        ),
    ]
