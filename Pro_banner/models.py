from django.db import models


class Pro_Banner(models.Model):
    product_image = models.ImageField(null=True,upload_to='images/')
    updated_at = models.DateTimeField(auto_now=True)
    Banner_name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Banner_name