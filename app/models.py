from django.db import models

# Create your models here.
class AboutModel(models.Model):
    
    about_story_img = models.ImageField(upload_to='about/', null=True, blank=True)
    
    card_1_img = models.ImageField(upload_to='about/', null=True, blank=True)
    
    card_2_img = models.ImageField(upload_to='about/', null=True, blank=True)
    
    card_3_img = models.ImageField(upload_to='about/', null=True, blank=True)
    
    card_4_img = models.ImageField(upload_to='about/', null=True, blank=True)
    
    designer_img = models.ImageField(upload_to='about/', null=True, blank=True)
    
    def __str__(self):
        return ("about images")
    
class ContactUsModel(models.Model):
    
    name = models.CharField(max_length=50,null=True)
    
    email = models.EmailField()
    
    ph_number = models.CharField(max_length=20,null=True)
    
    subject = models.CharField(max_length=200,null=True)
    
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject
    
class ContactSettingModel(models.Model):
    
    contact_top_img = models.ImageField(upload_to='contact/',null=True,blank=True)
    
    contact_bottom_img = models.ImageField(upload_to='contact/',null=True,blank=True)