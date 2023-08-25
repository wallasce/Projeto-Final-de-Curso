from django.db import models

# Create your models here.
class Controler(models.Model):
    ki = models.FloatField()
    kp = models.FloatField()
    setPoint = models.FloatField()