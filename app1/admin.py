from django.contrib import admin

from app1.models import ModelFilm


class AdminFilm(admin.ModelAdmin):
    list_display = ("id", "name", "year", "author", "english", "land_production", "official_page")


admin.site.register(ModelFilm, AdminFilm)