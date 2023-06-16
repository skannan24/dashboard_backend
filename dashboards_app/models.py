from django.db import models


# Create your models here.

class Dashboards(models.Model):
    name = models.CharField(unique=True, max_length=40)
    description = models.CharField(max_length=80, null=True, blank=True)

    class Meta:
        db_table = 'dashboards'
