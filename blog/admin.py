from django.contrib import admin

# Register your models here.
from .models import Bloger, Comment, Blog

admin.site.register(Bloger)
admin.site.register(Comment)
admin.site.register(Blog)