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


class NavBar(models.Model):
    def __str__(self):
        return "Nav Bar"


class NavSection(models.Model):
    bar = models.ForeignKey(NavBar, on_delete=models.CASCADE)
    section_text = models.CharField(max_length=50)
    section_link = models.FilePathField(path=local_path("prof_site_app/templates/prof_site_app"))
    section_label = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.section_text)


class Company(models.Model):
    logo_picture_path = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)


class Experience(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return "{}".format(self.title)

class PursuitType(models.Model):
    type = models.CharField(max_length=25)

    @classmethod
    def get_default_pk(cls):
        pursuit_type, created = cls.objects.get_or_create(
            type = "Erroneous"
        )
        return pursuit_type.pk


    def __str__(self):
        return "{}".format(self.type)


class Pursuit(models.Model):
    pursuit_type = models.ForeignKey(PursuitType, on_delete=models.SET_DEFAULT, default=PursuitType.get_default_pk)
    internal_label = models.CharField(max_length=50)
    img_path = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    @classmethod
    def get_default_pk(cls):
        pursuit, created = cls.objects.get_or_create(
            internal_label = "Filler Pursuit",
            defaults = dict(img_path="filler_image_path",
                            title="Filler Title",
                            description="Filler Description"))
        return pursuit.pk

    def __str__(self):
        return "{}".format(self.internal_label)


class BlogPost(models.Model):
    pursuit = models.ForeignKey(Pursuit, on_delete=models.SET_DEFAULT, default=Pursuit.get_default_pk(), blank=True, null=True)
    title = models.CharField(max_length=50)
    date = models.DateField()
    preview = models.CharField(max_length=200)
    article = models.TextField()

    def __str__(self):
        return "{}".format(self.title)


class Link(models.Model):
    pursuit = models.ForeignKey(Pursuit, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=30)
    link = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.text)
