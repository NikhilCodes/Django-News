# Generated by Django 3.1 on 2020-08-10 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20200810_0525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='time',
        ),
    ]
