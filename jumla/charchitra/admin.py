from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Actor)
admin.site.register(Genre)
# admin.site.register(Duration)
admin.site.register(Video)
admin.site.register(VideoPrice)
admin.site.register(VideoPackPrice)
admin.site.register(Subscribe)