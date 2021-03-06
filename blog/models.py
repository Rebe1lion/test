from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(blank = True, null = True)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    birthday = models.DateField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name



