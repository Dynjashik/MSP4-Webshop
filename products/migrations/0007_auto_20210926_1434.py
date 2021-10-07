# Generated by Django 3.2.7 on 2021-09-26 14:34
# flake8: noqa
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210926_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envcategory',
            name='friendly_name',
            field=models.CharField(blank=True, default=[], max_length=254),
        ),
        migrations.RemoveField(
            model_name='product',
            name='env_category',
        ),
        migrations.AddField(
            model_name='product',
            name='env_category',
            field=models.ManyToManyField(blank=True, to='products.EnvCategory'),
        ),
    ]
