from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your models here.
#change form register
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class Painting(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()
    upload_date = models.DateTimeField(auto_now_add=True)
    