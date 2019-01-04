from django.shortcuts import render
from django.db import IntegrityError
from django.http import Http404
from scraping.utils import *
from scraping.models import *
from scraping.forms import FindVacancyForm
import datetime

# Create your views here.


def index(request):
    return render(request, 'base.html')


def list_v(request):
    today = datetime.date.today()
    city = City.objects.get(name='Kyiv')
    specialty = Specialty.objects.get(name='Python')
    qs = Vacancy.objects.filter(city=city.id, specialty=specialty.id, date=today)
    if qs:
        return render(request, 'scraping/list.html', {'jobs': qs})
    return render(request, 'scraping/list.html')


def vacancy_list(request):
    today = datetime.date.today()
    form = FindVacancyForm
    if request.GET:
        try:
            city_id = int(request.GET.get('city'))
            specialty_id = int(request.GET.get('specialty'))
        except ValueError:
            raise Http404('Page not found')
        context = {}
        context['form'] = form
        qs = Vacancy.objects.filter(city=city_id, specialty=specialty_id, date=today)
        if qs:
            context['jobs'] = qs
            return render(request, 'scraping/list.html', context)
    return render(request, 'scraping/list.html', {'form': form})


def home(request):
    city = City.objects.get(name='Kyiv')
    specialty = Specialty.objects.get(name='Python')
    url_set = Url.objects.filter(city=city, specialty=specialty)
    website = Website.objects.all()
    url_djinni = url_set.get(website=website.get(name='Djinni.co')).url
    url_rabota = url_set.get(website=website.get(name='Rabota.ua')).url
    url_work = url_set.get(website=website.get(name='Work.ua')).url
    url_dou = url_set.get(website=website.get(name='Dou.ua')).url

    jobs = []
    jobs.extend(djinni(url_djinni))
    jobs.extend(rabota(url_rabota))
    jobs.extend(work(url_work))
    jobs.extend(dou(url_dou))
    # v = Vacancy.objects.filter(city=city.id, specialty=specialty.id).values('url')
    # url_list = [i['url'] for i in v]
    for job in jobs:
        # if job['href'] not in url_list:
        vacancy = Vacancy(city=city, specialty=specialty, url=job['href'], title=job['title'],
                              description=job['desc'], company=job['company'])
        try:
            vacancy.save()
        except IntegrityError:
            pass

    return render(request, 'scraping/list.html', {'jobs': jobs})