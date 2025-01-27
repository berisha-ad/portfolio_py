from django.db import models


class project(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=150)
    imagelink = models.ImageField(
        upload_to='images/%Y/%m/%d')
    date = models.CharField(max_length=150)
    skills = models.CharField(max_length=150)
    link = models.CharField(max_length=250)


class backend_skill(models.Model):
    title = models.CharField(max_length=150)
    iconlink = models.FileField(upload_to='svg/%Y/%m/%d')


class frontend_skill(models.Model):
    title = models.CharField(max_length=150)
    iconlink = models.FileField(upload_to='svg/%Y/%m/%d')


class tool(models.Model):
    title = models.CharField(max_length=150)
    iconlink = models.FileField(upload_to='svg/%Y/%m/%d')


class file(models.Model):
    cvlink = models.FileField(upload_to='files/%Y/%m/%d')
    filename = models.CharField(max_length=150, null=True)
