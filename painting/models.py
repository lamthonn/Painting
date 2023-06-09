from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor_uploader.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


# Create your models here.
#change form register
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class Painting(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(widget=CKEditorWidget())
    image = models.ImageField()
    upload_date = models.DateTimeField(auto_now_add=True)
    imagelq = models.ImageField()
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    cmt = models.TextField()