# Generated by Django 3.1 on 2020-08-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subtitle',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
