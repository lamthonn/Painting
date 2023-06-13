from django.contrib import admin
from .models import Painting, Comment, Like, avatar

# Register your models here.
admin.site.register(Painting)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(avatar)