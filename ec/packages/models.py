from django.db import models
from django.utils import timezone


class Packages(models.Model):
    id = models.AutoField(primary_key=True)
    vpnName = models.CharField(max_length=15)
    isStarred = models.BooleanField(default=False)
    starredDetail = models.CharField(max_length=255)
    discount = models.CharField(max_length=255)
    planDuration = models.CharField(blank=False, max_length=255)
    isCutCost = models.BooleanField(default=False)
    cutCost = models.CharField(max_length=15)
    originalCost = models.CharField(max_length=15)
    planDetail = models.CharField(max_length=255)
    miscDetail = models.CharField(max_length=255)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.vpnName} - {self.planDuration}"
