import json
import re
import urllib.parse
import urllib.request

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from beyond_aviation import settings
from beyond_aviation.settings import MEDIA_URL
from .models import Service, ServiceOffering, Section, SubSection, Menu, QueryForm, Page, Setting, Slider, Slides


# Fetch Common Object Data Method
def fetch_common_object_data():
    menus = Menu.objects.filter(status="active").order_by('sequence')
    pages = Page.objects.filter(status="active")
    offerings = ServiceOffering.objects.filter(status="active")
    services = Service.objects.filter(status="active")
    owner_section = Section.objects.filter(section_type="owner", status="active")
    other_sections = Section.objects.filter(section_type="other", status="active")
    sub_sections = SubSection.objects.filter(status="active")
    sliders = Slider.objects.filter(status="active")
    slides = Slides.objects.filter(status="active")
    setting = Setting.objects.all()
    fav_icon = ""
    for sett in setting:
        fav_icon = sett.fav_icon

    pair_first_values = []
    for i in range(0, len(offerings), 2):
        pair_first_values.append(offerings[i])

    pair_second_values = []
    for i in range(1, len(offerings), 2):
        pair_second_values.append(offerings[i])

    max_length = max(len(pair_first_values), len(pair_second_values))
    offerings_pair_list = []
    for i in range(max_length):
        try:
            first_val = pair_first_values[i]
        except IndexError:
            first_val = None
        try:
            second_val = pair_second_values[i]
        except IndexError:
            second_val = None
        offerings_pair_list.append([first_val, second_val])

    common_obj_data = {
        'menus': menus,
        'pages': pages,
        'settings': setting,
        'services': services,
        'offerings': offerings_pair_list,
        'owner_section': owner_section,
        'other_sections': other_sections,
        'sub_sections': sub_sections,
        'media_url': MEDIA_URL,
        'fav_icon': fav_icon,
        'sliders': sliders,
        'slides': slides
    }

    return common_obj_data


# Server Error 500 Handler View
def error_500_view(request):
    template = loader.get_template('error_page.html')
    context = fetch_common_object_data()

    return HttpResponse(template.render(context, request))


# Page Not Found Error 404 Handler View
def error_404_view(request, exception):
    template = loader.get_template('error_page.html')
    context = fetch_common_object_data()

    return HttpResponse(template.render(context, request))


# Homepage / Index View
def index(request):
    template = loader.get_template('homepage.html')
    context = fetch_common_object_data()

    return HttpResponse(template.render(context, request))


# View Page Detail
def view_page(request, slug):
    template = loader.get_template('pages.html')
    context = fetch_common_object_data()
    if slug != 'undefined':
        get_page_id = Page.objects.get(slug=slug)
        context['get_page_id'] = get_page_id

    return HttpResponse(template.render(context, request))


# View Service Detail
def view_service(request, slug):
    get_service_id = Service.objects.get(slug=slug)

    template = loader.get_template('view_service.html')
    context = fetch_common_object_data()
    context['get_service_id'] = get_service_id

    return HttpResponse(template.render(context, request))


# Query Form View
def query_form(request):
    logo = Menu.objects.filter(status="active")
    if request.method == "POST":
        contact_regex = re.compile(
            r'(^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$)')

        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        name_regex = re.compile(
            r"(^[A-Za-z]+$)")

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:
            if not re.fullmatch(contact_regex, phone):
                messages.info(request, 'Invalid Phone')
            elif not re.fullmatch(email_regex, email):
                messages.info(request, 'Invalid Email')
            elif not re.fullmatch(name_regex, first_name) or not re.fullmatch(name_regex, last_name):
                messages.info(request, 'Invalid Name')
            else:
                query_id = QueryForm(first_name=first_name, last_name=last_name, email=email, phone=phone,
                                     message=message)

                send_mail(' Above & Beyond - Contact Form',
                          message,
                          email,
                          ['goabovebeyondaviation@gmail.com'],
                          fail_silently=False,
                          html_message=loader.render_to_string(
                              'email_template.html',
                              {
                                  'first_name': first_name,
                                  'last_name': last_name,
                                  'email': email,
                                  'phone': phone,
                                  'message': message,
                                  'logo': logo,
                                  'media_url': MEDIA_URL,
                              }
                          ))
                if send_mail:
                    query_id.email_as_send = True
                query_id.save()

                messages.success(request, 'Thankyou for Contacting us.')
        else:
            messages.info(request, 'Please verify that you are not a robot.')

        return redirect(request.META['HTTP_REFERER'])
    return redirect(request.META['HTTP_REFERER'])
