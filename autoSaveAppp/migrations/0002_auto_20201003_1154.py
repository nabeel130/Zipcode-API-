# Generated by Django 3.1.2 on 2020-10-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoSaveAppp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='zip_code',
            field=models.IntegerField(max_length=6),
        ),
    ]
