from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=150)
    imagelink = models.ImageField(
        upload_to='images/%Y/%m/%d')
    date = models.CharField(max_length=150)
    skills = models.CharField(max_length=150)
    link = models.CharField(max_length=250)
    sort_order = models.IntegerField(default=0)


class Backend_skill(models.Model):
    title = models.CharField(max_length=150)
    iconlink = models.FileField(upload_to='svg/%Y/%m/%d')


class Frontend_skill(models.Model):
    title = models.CharField(max_length=150)
    iconlink = models.FileField(upload_to='svg/%Y/%m/%d')


class Tool(models.Model):
    title = models.CharField(max_length=150)
    iconlink = models.FileField(upload_to='svg/%Y/%m/%d')


class File(models.Model):
    cvlink = models.FileField(upload_to='files/%Y/%m/%d')
    filename = models.CharField(max_length=150, null=True)
