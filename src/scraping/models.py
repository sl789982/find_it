from django.db import models


# Create your models here


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='City')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class Specialty(models.Model):
    name = models.CharField(max_length=50, verbose_name='Specialty')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Specialities'


class Vacancy(models.Model):
    url = models.CharField(max_length=250, verbose_name='URL', unique=True)
    title = models.CharField(max_length=250, verbose_name='Title')
    description = models.TextField(verbose_name='Description', blank=True)
    company = models.CharField(max_length=250, verbose_name='Company', blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='City')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name='Specialty')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Jobs'

