from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'city', 'specialty', 'is_active')
    list_editable = ['is_active']

    class Meta:
        model = Subscriber


admin.site.register(Subscriber,SubscriberAdmin)


