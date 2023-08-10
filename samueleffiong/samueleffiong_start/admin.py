from django.contrib import admin

from .models import Country, Schools, village, State, Local_Government

# Register your models here.
admin.site.register(Country)
admin.site.register(Schools)
admin.site.register(village)
admin.site.register(State)
admin.site.register(Local_Government)
