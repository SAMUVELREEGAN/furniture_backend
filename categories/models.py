from django.db import models

class Category(models.Model):
    categorie = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.categorie
