# Generated by Django 4.2.1 on 2023-07-27 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0006_alter_kolegij_options_alter_obavijest_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obavijest',
            name='autor',
        ),
    ]
