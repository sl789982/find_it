from django.db import models
from scraping.models import City, Specialty


# Create your models here.


class Subscriber(models.Model):
    email = models.CharField(max_length=100, unique=True, verbose_name='e-mail')
    city = models.ForeignKey(City, verbose_name='City', on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, verbose_name='Specialty', on_delete=models.CASCADE)
    password = models.CharField(max_length=25, verbose_name='Password')
    is_active = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Subscribers'
