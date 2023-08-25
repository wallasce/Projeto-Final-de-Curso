from django.db import models

# Create your models here.
class Controller(models.Model):
    ki = models.FloatField()
    kp = models.FloatField()
    setPoint = models.FloatField()