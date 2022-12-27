from colorfield.fields import ColorField
from django.db import models
from django.utils.safestring import mark_safe
from tinymce import HTMLField

# Create your models here.

CHOICES = (
    ('left', 'Left'),
    ('right', 'Right')
)

SECTIONS = (
    ('other', 'Other'),
    ('owner', 'Owner'),
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
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        db_table = 'services'

    def __str__(self):
        return self.name

    def image_preview(self):
        return mark_safe('<img src="{url}" width="300" height="200"/>'.format(url=self.image.url))


class ServiceOffering(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='ServiceOffering')
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
        return mark_safe('<img src="{url}" width="80" height="80"/>'.format(url=self.icon.url))


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, unique=True)
    header_img = models.ImageField(upload_to='HeaderImage', null=True, blank=True, verbose_name='Header Image')
    content = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pages'
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def header_image_preview(self):
        return mark_safe('<img src="{url}" width="200" height="150"/>'.format(url=self.header_img.url))


class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    text_align = models.CharField(max_length=10, choices=CHOICES, default='left')
    section_type = models.CharField(max_length=20, choices=SECTIONS, default='other')
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')
    image = models.ImageField(upload_to='Section', null=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)
    show_mail_us_button = models.BooleanField(default=False, verbose_name='Show Mail Us Button')
    background_color = ColorField(default='#FFFFFFFF', format="hexa")
    text_color = ColorField(default='#FFFFFFFF', format="hexa")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'section'
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def image_preview(self):
        return mark_safe('<img src="{url}" width="320" height="300"/>'.format(url=self.image.url))


class SubSection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    content = models.TextField()
    icon = models.ImageField(upload_to='SubSection', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sub_section'
        ordering = ['created_on']

    def __str__(self):
        return self.section.title

    def icon_preview(self):
        return mark_safe('<img src="{url}" width="80" height="80"/>'.format(url=self.icon.url))


class Menu(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(null=True, unique=True)
    sequence = models.IntegerField(default=0)
    show_in_footer = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='inactive')

    class Meta:
        db_table = 'menu'
        ordering = ['created_on']

    def __str__(self):
        return self.name


class QueryForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50, null=True)
    message = models.TextField()
    email_as_send = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'query_form'
        ordering = ['created_on']

    def __str__(self):
        return self.first_name


class Setting(models.Model):
    contact_address = HTMLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    homepage_logo = models.ImageField(upload_to='HomepageLogo', null=True, blank=True)
    footer_logo = models.ImageField(upload_to='FooterLogo', null=True, blank=True)
    fav_icon = models.ImageField(upload_to='FavIcon', null=True, blank=True)
    common_service_content = HTMLField(null=True, blank=True)

    class Meta:
        db_table = "setting"
