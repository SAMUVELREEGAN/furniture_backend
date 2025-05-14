from django.db import models


class Logo(models.Model):
    picture = models.ImageField(null=True,upload_to='images/')
    updated_at = models.DateTimeField(auto_now=True)
    logo_name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.logo_name