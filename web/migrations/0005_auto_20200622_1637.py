# Generated by Django 3.0.4 on 2020-06-22 16:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200622_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='VnData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_type', models.CharField(choices=[('CT', 'CITIES'), ('PT', 'PATIENTS')], default='CITIES', max_length=2)),
                ('date', models.DateField(default=datetime.datetime(2020, 6, 22, 16, 37, 31, 396327, tzinfo=utc))),
                ('csv_file', models.FileField(upload_to='data/uploads/VN')),
            ],
        ),
        migrations.AlterField(
            model_name='jhudata',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 16, 37, 31, 396019, tzinfo=utc)),
        ),
    ]
