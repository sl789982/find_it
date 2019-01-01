from django.shortcuts import render
from django.db import IntegrityError
from scraping.utils import *
from scraping.models import *

# Create your views here.


def home(request):
    jobs = []
    jobs.extend(djinni())
    jobs.extend(rabota())
    jobs.extend(work())
    jobs.extend(dou())
    city = City.objects.get(name='Kyiv')
    specialty = Specialty.objects.get(name='Python')
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

    return render(request, 'base.html', {'jobs': jobs})