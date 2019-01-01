from django.shortcuts import render
from .utils import *
from .models import *

# Create your views here.


def home(request):
    jobs = djinni()
    city = City.objects.get(name='Kyiv')
    specialty = Specialty.objects.get(name='Python')
    v = Vacancy.objects.filter(city=city.id, specialty=specialty.id).values('url')
    url_list = [i['url'] for i in v]
    for job in jobs:
        if job['href'] not in url_list:
            vacancy = Vacancy(city=city, specialty=specialty, url=job['href'], title=job['title'],
                              description=job['desc'], company=job['company'])
            vacancy.save()

    return render(request, 'base.html', {'jobs': jobs})