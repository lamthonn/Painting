# Generated by Django 4.1.5 on 2023-06-08 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        # ('painting', '0004_like_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avt', models.ImageField(default='https://cdn-icons-png.flaticon.com/512/149/149071.png', upload_to='media/avatar')),
                ('user_painting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
