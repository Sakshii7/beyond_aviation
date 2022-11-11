from django.db import models


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=1000)
    excerpt = models.CharField(max_length=1000, null=True)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='pics', null=True)

    def __str__(self):
        return self.name


class ServiceOffering(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='icons', null=True)

    def __str__(self):
        return self.title
