from django.db import models
from .validators import validate_file_extension


class TgUser(models.Model):
    phone = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    family_status = models.CharField(max_length=20, blank=True, null=True)
    age = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='user')
    type = models.CharField(max_length=40, blank=True, null=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Admin(models.Model):
    chat_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.chat_id)


class Info(models.Model):
    text = models.TextField()
    video_id = models.CharField(max_length=255)
    # video = models.FileField(upload_to='video/', validators=[validate_file_extension])

    def __str__(self):
        return str(self.text)
