from django.db import models

# Create your models here.
class Articles(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[0:50]+'...'    
