from django.db import models

class WebLink(models.Model):
    link_name = models.CharField(max_length=100)

    def __str__(self):
        return self.link_name
