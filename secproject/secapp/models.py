from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    date_posted = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'