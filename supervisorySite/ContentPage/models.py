from django.db import models

# Create your models here.
class HelpContent(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=255)
    fontAwesome = models.CharField(max_length=50)

class HomeCard(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=255)
    fontAwesome = models.CharField(max_length=50)

class HomeCardExtra(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=255)
    fontAwesome = models.CharField(max_length=50)