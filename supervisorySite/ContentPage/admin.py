from django.contrib import admin

from .models import HelpContent, HomeCard, HomeCardExtra
# Register your models here.
admin.site.register(HelpContent)
admin.site.register(HomeCard)
admin.site.register(HomeCardExtra)