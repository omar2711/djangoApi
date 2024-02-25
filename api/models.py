from django.db import models


class RegionServer(models.Model):
    pid = models.CharField(max_length=50, primary_key=True)
    port = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)
    totalSpace = models.CharField(max_length=50)
    freeSpace = models.CharField(max_length=50)
    usedSpace = models.CharField(max_length=50)
