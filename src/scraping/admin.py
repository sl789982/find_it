from django.contrib import admin
from .models import *

# Register your models here.


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'city', 'specialty', 'date')

    class Meta:
        model = Vacancy




admin.site.register(City)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Specialty)
admin.site.register(Website)
admin.site.register(Url)