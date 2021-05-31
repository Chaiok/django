from django.contrib import admin

# Register your models here.
from .models import Manufacturer,GPU,Videokart

admin.site.register(Manufacturer)
admin.site.register(GPU)
admin.site.register(Videokart)