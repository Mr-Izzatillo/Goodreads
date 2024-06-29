from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic', default='defoult_profile_pic.jpg')


    def check_hash_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)
            
            
            
    def save(self,  *args, **kwargs):
        self.check_hash_password()
        super().save(*args, **kwargs)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    email = models.EmailField() 
    country = models.TextField()
    region = models.TextField()
    
           