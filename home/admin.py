from django.contrib import admin
from home.models import Contact
from home.models import Detail
from .models import College_Info

# Register your models here.
admin.site.register(Contact)
admin.site.register(Detail)  
admin.site.register(College_Info)  