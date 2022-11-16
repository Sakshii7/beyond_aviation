from django.http import HttpResponse
from django.template import loader

from beyond_aviation.settings import  MEDIA_URL
from .models import Service, ServiceOffering, Section, SubSection


# Create your views here.


def index(request):
    services = Service.objects.all().values()
    offerings = ServiceOffering.objects.all()
    sections = Section.objects.all()
    sub_sections = SubSection.objects.all()
    template = loader.get_template('homepage.html')
    context = {
        'services': services,
        'offerings': offerings,
        'sections': sections,
        'sub_sections': sub_sections,
        'media_url': MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))


def view_service(request, slug):
    get_service_id = Service.objects.get(slug=slug)
    template = loader.get_template('view_service.html')
    context = {
        'get_service_id': get_service_id,
    }
    return HttpResponse(template.render(context, request))