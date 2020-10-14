from django.db import models

class File(models.Model):

  file = models.FileField(blank=False, null=False)
  name = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)

class Check(models.Model):

  file = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)

