from django.db import models

# Create your models here.
class Painting(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()
    upload_date = models.DateTimeField(auto_now_add=True)
    