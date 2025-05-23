# Create your models here.
from django.db import models

class Review(models.Model):
    profile_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='review_pics/')
    message = models.TextField()
    point = models.IntegerField()

    def __str__(self):
        return self.profile_name
