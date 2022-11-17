from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

CHOICES = (
    ("left", "Left"),
    ("right", "Right")
)

SECTIONS = (
    ("other", "Other"),
    ("owner", "Owner")
)


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


class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    text_align = models.CharField(max_length=10, choices=CHOICES, default=0)
    section_type = models.CharField(max_length=10, choices=SECTIONS, default=0)
    image = models.ImageField(upload_to='section_images', null=True)
    created_on = models.DateTimeField(null=True)

    class Meta:
        db_table = 'section'
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def section_image_preview(self):
        return mark_safe('<img src="{url}" width="80" height="80"/>'.format(url=self.image.url))


class SubSection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    content = models.TextField()
    section_icon = models.ImageField(upload_to='section_icons', null=True, blank=True)
    created_on = models.DateTimeField(null=True)

    class Meta:
        db_table = 'sub_section'
        ordering = ['created_on']

    def __str__(self):
        return self.section.title

    def section_icon_preview(self):
        return mark_safe('<img src="{url}" width="80" height="80"/>'.format(url=self.section_icon.url))
