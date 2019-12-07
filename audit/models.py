from django.db import models

# -------------------------------------------------------------
class audit(models.Model):
    dateTime = models.CharField(max_length=32, null=False,blank=False)
    password = models.CharField(max_length=50, null=False,blank=False)
    a = models.CharField(max_length=50, null=True,blank=True)
