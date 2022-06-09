from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username', 'email')

@admin.register(Shape)
class ShapeAdmin(admin.ModelAdmin):
    list_display=('name', 'side', 'height', 'base')

