from django.contrib import admin

# Register your models here.
from .models import Painting, Tag, Review


admin.site.register(Painting)
admin.site.register(Review)
admin.site.register(Tag)
