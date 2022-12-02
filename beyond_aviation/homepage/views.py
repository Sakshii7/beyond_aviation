from django.http import HttpResponse
from django.template import loader

from beyond_aviation.settings import MEDIA_URL
from .models import Service, ServiceOffering, Section, SubSection, Menu, Contact, Page


# Create your views here.


def index(request):
    services = Service.objects.filter(status="active")
    offerings = ServiceOffering.objects.filter(status="active")
    owner_section = Section.objects.filter(section_type="owner", status="active")
    other_section = Section.objects.filter(section_type="other", status="active")
    sub_sections = SubSection.objects.filter(status="active")
    homepage_logo = ServiceOffering.objects.filter(status="inactive")
    menus = Menu.objects.filter(status="active")
    contacts = Contact.objects.filter(status="active")
    pages = Page.objects.filter(status="active")
    template = loader.get_template('homepage.html')
    context = {
        'services': services,
        'offerings': offerings,
        'owner_section': owner_section,
        'other_section': other_section,
        'sub_sections': sub_sections,
        'homepage_logo': homepage_logo,
        'menus': menus,
        'pages': pages,
        'media_url': MEDIA_URL,
        'contacts': contacts
    }
    return HttpResponse(template.render(context, request))


def view_service(request, slug):
    get_service_id = Service.objects.get(slug=slug)
    services = Service.objects.filter(status="active")
    owner_section = Section.objects.filter(section_type="owner", status="active")
    menus = Menu.objects.filter(status="active")
    contacts = Contact.objects.filter(status="active")
    offerings = ServiceOffering.objects.filter(status="active")
    template = loader.get_template('view_service.html')
    context = {
        'get_service_id': get_service_id,
        'offerings': offerings,
        'services': services,
        'owner_section': owner_section,
        'menus': menus,
        'contacts': contacts,
        'media_url': MEDIA_URL,

    }
    return HttpResponse(template.render(context, request))


def view_pages(request, slug):
    get_page_id = Page.objects.get(slug=slug)
    services = Service.objects.filter(status="active")
    owner_section = Section.objects.filter(section_type="owner", status="active")
    menus = Menu.objects.filter(status="active")
    contacts = Contact.objects.filter(status="active")
    offerings = ServiceOffering.objects.filter(status="active")
    template = loader.get_template('pages.html')

    context = {
        'get_page_id': get_page_id,
        'offerings': offerings,
        'services': services,
        'owner_section': owner_section,
        'menus': menus,
        'contacts': contacts,
        'media_url': MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))
