# Generated by Django 3.2.7 on 2021-10-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_sent',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
