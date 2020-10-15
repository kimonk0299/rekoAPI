from django.db import models

class File(models.Model):

  file = models.FileField(blank=False, null=False)
  visitor_name = models.CharField(max_length=20,null=False)
  company_name = models.CharField(max_length=20,null=False)
  whom_to_meet = models.EmailField(max_length=254,null=False)
  visitor_phone_no = models.IntegerField(null=False)
  visitor_email = models.EmailField(max_length=254,null=False)
  timestamp = models.DateTimeField(auto_now_add=True)

class Check(models.Model):

  file = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)

