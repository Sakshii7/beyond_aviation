import json
import os
import re

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.core.mail import EmailMessage, send_mail

from beyond_aviation import settings
from beyond_aviation.settings import MEDIA_URL, EMAIL_HOST_USER
from .models import Service, ServiceOffering, Section, SubSection, Menu, QueryForm, Page, Setting


# Create your views here.


def index(request):
    services = Service.objects.filter(status="active")
    offerings = ServiceOffering.objects.filter(status="active")
    owner_section = Section.objects.filter(section_type="owner", status="active")
    other_section = Section.objects.filter(section_type="other", status="active")
    sub_sections = SubSection.objects.filter(status="active")
    homepage_logo = ServiceOffering.objects.filter(status="inactive")
    menus = Menu.objects.filter(status="active")
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
    }
    return HttpResponse(template.render(context, request))


def view_service(request, slug):
    get_service_id = Service.objects.get(slug=slug)
    services = Service.objects.filter(status="active")
    owner_section = Section.objects.filter(section_type="owner", status="active")
    canada_jetline_section = Section.objects.filter(section_type="canada_jetline", status="active")
    menus = Menu.objects.filter(status="active")
    offerings = ServiceOffering.objects.filter(status="active")
    pages = Page.objects.filter(status="active")
    template = loader.get_template('view_service.html')
    with open("sample.json") as jsonFile:
        data = json.load(jsonFile)
    context = {
        'get_service_id': get_service_id,
        'offerings': offerings,
        'services': services,
        'owner_section': owner_section,
        'menus': menus,
        'canada_jetline_section': canada_jetline_section,
        'pages': pages,
        'media_url': MEDIA_URL,
        'data': data.get("address")


    }
    return HttpResponse(template.render(context, request))


def view_pages(request, slug):
    get_page_id = Page.objects.get(slug=slug)
    services = Service.objects.filter(status="active")
    owner_section = Section.objects.filter(section_type="owner", status="active")
    canada_jetline_section = Section.objects.filter(section_type="canada_jetline", status="active")
    sub_sections = SubSection.objects.filter(status="active")
    menus = Menu.objects.filter(status="active")
    offerings = ServiceOffering.objects.filter(status="active")
    pages = Page.objects.filter(status="active")
    system_data = Setting.objects.all()
    template = loader.get_template('pages.html')
    # with open("sample.json") as jsonFile:
    #     data = json.load(jsonFile)
    context = {
        'get_page_id': get_page_id,
        'offerings': offerings,
        'services': services,
        'owner_section': owner_section,
        'menus': menus,
        'canada_jetline_section': canada_jetline_section,
        'sub_sections': sub_sections,
        'media_url': MEDIA_URL,
        'pages': pages,
        'system_data': system_data
    }
    return HttpResponse(template.render(context, request))


def query_form(request):
    logo = Menu.objects.filter(status="active")
    if request.method == "POST":
        contact_regex = re.compile(
            r'(^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$)')

        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        name_regex = re.compile(
            r"(^[A-Za-z]+$)")

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if not re.fullmatch(contact_regex, phone):
            messages.error(request, 'Invalid Phone')
        elif not re.fullmatch(email_regex, email):
            messages.error(request, 'Invalid Email')
        elif not re.fullmatch(name_regex, first_name) or not re.fullmatch(name_regex, last_name):
            messages.error(request, 'Invalid Name')
        else:
            query_id = QueryForm(first_name=first_name, last_name=last_name, email=email, phone=phone, message=message)
            query_id.save()
            send_mail(' Above & Beyond - Contact Form',
                      message,
                      email,
                      ['sakshi.chandel@socialmediafreaks.com'],
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
                      )
                      )
            messages.success(request, 'Thankyou for Contacting us.')
        return redirect(request.META['HTTP_REFERER'])
    return redirect(request.META['HTTP_REFERER'])
