from django.db import models

class Visits(models.Model):

    short_url = models.CharField(max_length=1000, null=True)
    request_type = models.CharField(max_length=1000, null=True)
    date = models.DateTimeField(null=True)
    user = models.CharField(max_length=1000, null=True)
    long_url = models.CharField(max_length=10000, null=True)
    menu_number = models.IntegerField(null=True)
    menu_type = models.CharField(max_length=1000, null=True)
