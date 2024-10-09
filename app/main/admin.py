from django.contrib import admin

from .models import Services


@admin.register(Services)
class ServiseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
