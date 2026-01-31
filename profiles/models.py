from django.db import models

# Create your models here.

class Profile(models.Model):
    user_image = models.ImageField(upload_to='uploads/')
