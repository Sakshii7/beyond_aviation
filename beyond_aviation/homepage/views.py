from django.http import HttpResponse
from django.template import loader

from beyond_aviation.settings import IMAGE_URL
from .models import Service, ServiceOffering


# Create your views here.


def index(request):
    services = Service.objects.all().values()
    offerings = ServiceOffering.objects.all()
    template = loader.get_template('homepage.html')
    context = {
        'services': services,
        'offerings': offerings,
        'media_url': IMAGE_URL
    }
    return HttpResponse(template.render(context, request))

