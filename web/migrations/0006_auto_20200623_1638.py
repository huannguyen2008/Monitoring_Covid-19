# Generated by Django 3.0.7 on 2020-06-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200622_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jhudata',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vndata',
            name='date',
            field=models.DateField(),
        ),
    ]
