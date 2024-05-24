import os

from django.db import models
from django.conf import settings


def local_path(local_dir: str) -> str:
    return os.path.join(settings.LOCAL_FILE_DIR, local_dir)


class HomePage(models.Model):
    headline = models.CharField(max_length=50)
    subtitle_1 = models.CharField(max_length=100)
    subtitle_2 = models.CharField(max_length=100)
    picture_path = models.CharField(max_length=100)

    def __str__(self):
        return "Home Page"


class Button(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.CASCADE)
    button_link = models.FilePathField(path=local_path("prof_site_app/templates/prof_site_app"))
    button_text = models.CharField(max_length=20)

    def __str__(self):
        return self.button_text


class Icon(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.CASCADE)
    icon_link = models.CharField(max_length=300)
    icon_img_path = models.CharField(max_length=100)
    icon_name = models.CharField(max_length=30)

    def __str__(self):
        return self.icon_name
