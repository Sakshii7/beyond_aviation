from django.db import models


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=50)
    excerpt = models.TextField(max_length=450, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='pics', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'services'


class ServiceOffering(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='icons', null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'service_offering'
