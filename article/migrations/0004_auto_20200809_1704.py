# Generated by Django 3.1 on 2020-08-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200809_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='article_images/'),
        ),
    ]
