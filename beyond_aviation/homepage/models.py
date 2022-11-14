from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=50)
    excerpt = models.TextField(max_length=450, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='pics', null=True)
    slug = models.SlugField(null=True, unique=True)
    created_on = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    def image_preview(self):
        return mark_safe('<img src="{url}" width="300" height="200"/>'.format(url=self.image.url))

    class Meta:
        ordering = ['created_on']
        db_table = 'services'


class ServiceOffering(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='icons', null=True)
    created_on = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    def icon_preview(self):
        return mark_safe('<img src="{url}" width="80" height="80"/>'.format(url=self.image.url))

    class Meta:
        db_table = 'service_offering'
        ordering = ['created_on']
