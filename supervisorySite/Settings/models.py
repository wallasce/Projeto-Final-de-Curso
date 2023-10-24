from django.db import models

# Create your models here.
class EndPoint(models.Model):
    ipAddress = models.CharField(max_length=15)
    port = models.CharField(max_length=4)

    def __str__(self) -> str:
        return f"{self.ipAddress} + {self.port}"