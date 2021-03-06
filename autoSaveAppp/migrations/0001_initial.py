# Generated by Django 3.1.2 on 2020-10-03 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.IntegerField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9)),
            ],
        ),
    ]
