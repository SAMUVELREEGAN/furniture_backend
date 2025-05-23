from django.db import models

class Craft(models.Model):
    year = models.BigIntegerField(default=0)
    client = models.BigIntegerField(default=0)  # Fixed typo from "clinet"
    projects = models.BigIntegerField(default=0)
