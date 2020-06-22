# Generated by Django 3.0.7 on 2020-06-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='fileName',
        ),
        migrations.AddField(
            model_name='table',
            name='csv_file',
            field=models.FileField(default=None, upload_to='data/'),
            preserve_default=False,
        ),
    ]
