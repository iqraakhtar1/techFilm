from django.db import models

# Create your models here.

class Audio(models.Model):
    record = models.FileField()

    class Meta:
        #managed = False
        db_table = 'Audio'