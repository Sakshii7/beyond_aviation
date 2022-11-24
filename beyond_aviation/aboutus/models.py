from django.db import models

# Create your models here.
STATUS = (
    ('active', 'Active'),
    ('inactive', 'InActive'),
)


class Aboutus(models.Model):
    title = models.CharField(max_length=50)
    # slug = models.SlugField(null=True, unique=True)
    # excerpt = models.TextField(max_length=450, null=True)
    description = models.TextField()
    # image = models.ImageField(upload_to='Service')
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
        db_table = 'about'

    def __str__(self):
        return self.title
