from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to="articles/", blank=False, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    
    def snippest(self):
        if len(self.body) > 50:
            return self.body[:50] + '...'
        else:
            return self.body