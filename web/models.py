from django.db import models
from django.utils import timezone

# Create your models here.


class Table(models.Model):
    csv_file = models.FileField(upload_to='data/upload')

    def __str__(self):
        return self.csv_file.name


class JhuData(models.Model):
    date = models.DateField(default=timezone.now(), unique=True)
    csv_file = models.FileField(upload_to='data/uploads/JHU')

    def __str__(self):
        return str(self.date)


class VnData(models.Model):
    TYPE_CHOICES = [
        ('CT', 'CITIES'),
        ('PT', 'PATIENTS')
    ]
    data_type = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default='CITIES')
    date = models.DateField(default=timezone.now(), unique=True)
    csv_file = models.FileField(upload_to='data/uploads/VN')

    def __str__(self):
        return "%s %s" % (self.data_type, str(self.date))