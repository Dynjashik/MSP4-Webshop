# Generated by Django 3.2.7 on 2021-09-28 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210926_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envcategory',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
