# Generated by Django 3.2.7 on 2021-10-07 19:05
# flake8: noqa
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210928_1955'),
        ('contact', '0002_alter_contact_date_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
        ),
    ]
