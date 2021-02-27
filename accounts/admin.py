from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Trainer)
admin.site.register(Fitness)
admin.site.register(Member)


