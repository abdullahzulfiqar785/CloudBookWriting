from django.contrib import admin
from .models import Book, Section


# Registering models
admin.site.register(Book)
admin.site.register(Section)
