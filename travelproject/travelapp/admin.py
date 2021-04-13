from django.contrib import admin
from . models import place, blog, discount


# Register your models here.
admin.site.register(place)
admin.site.register(blog)
admin.site.register(discount)