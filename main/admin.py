from django.contrib import admin

# Register your models here.
from .models import Main, TODO

@admin.register(Main, TODO)
class HomeAdmin(admin.ModelAdmin):
    pass