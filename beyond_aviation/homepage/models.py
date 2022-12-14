from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

CHOICES = (
    ('left', 'Left'),
    ('right', 'Right')
)

SECTIONS = (
    ('other', 'Other'),
    ('owner', 'Owner'),
    ('canada_jetline', 'Canada Jetline Cargo')
)

STATUS = (
    ('active', 'Active'),
    ('inactive', 'InActive'),
)


class Service(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True)
    excerpt = models.CharField(max_length=450, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='Service', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_flag = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        db_table = 'services'

    def __str__(self):
        return self.slug

    def image_preview(self):
        return mark_safe('<img src="{url}" width="300" height="200"/>'.format(url=self.image.url))


class ServiceOffering(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='ServiceOffering')
    text_align = models.CharField(max_length=10, choices=CHOICES, default='left')
    show_on_about_page = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'service_offering'
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def icon_preview(self):
        return mark_safe('<img src="{url}" width="80" height="80"/>'.format(url=self.image.url))


class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    text_align = models.CharField(max_length=10, choices=CHOICES, default='left')
    section_type = models.CharField(max_length=20, choices=SECTIONS, default='other')
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')
    image = models.ImageField(upload_to='Section', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'section'
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def section_image_preview(self):
        return mark_safe('<img src="{url}" width="320" height="300"/>'.format(url=self.image.url))


class SubSection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    content = models.TextField()
    section_icon = models.ImageField(upload_to='SubSection', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sub_section'
        ordering = ['created_on']

    def __str__(self):
        return self.section.title

    def section_icon_preview(self):
        return mark_safe('<img src="{url}" width="80" height="80"/>'.format(url=self.section_icon.url))


class Menu(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(null=True, unique=True)
    show_in_footer = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Homepage Logo', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')

    class Meta:
        db_table = 'menu'
        ordering = ['created_on']

    def __str__(self):
        return self.name

    def logo_preview(self):
        return mark_safe('<img src="{url}" width="300" height="200"/>'.format(url=self.image.url))


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, unique=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    header_img = models.ImageField(upload_to='Header Image', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pages'
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def logo_preview(self):
        return mark_safe('<img src="{url}" width="300" height="200"/>'.format(url=self.header_img.url))


class QueryForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50, null=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'query_form'
        ordering = ['created_on']

    def __str__(self):
        return self.first_name


class Footer(models.Model):
    footer_logo = models.ImageField(upload_to='Footer Logo', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'footer'


class Setting(models.Model):
    class Meta:
        managed = False
        db_table = "auth_user"
        default_permissions = ('view')
