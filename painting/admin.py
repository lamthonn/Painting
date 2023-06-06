from django.contrib import admin
from .models import Painting, Comment, Like

# Register your models here.
admin.site.register(Painting)
admin.site.register(Comment)
admin.site.register(Like)