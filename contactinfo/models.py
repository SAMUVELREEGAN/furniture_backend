from django.db import models


class Info(models.Model):
    adress = models.CharField(max_length=200,null=True)
    ph_number = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    facebook_url = models.CharField(max_length=200,null=True)
    instagram_url = models.CharField(max_length=200,null=True)
    instagram_url = models.CharField(max_length=200,null=True)
    youtube_url = models.CharField(max_length=200,null=True)
    whatsapp_url = models.CharField(max_length=200,null=True)

    def __str__(self):
        return f"{self.adress} - {self.ph_number} - {self.email}"