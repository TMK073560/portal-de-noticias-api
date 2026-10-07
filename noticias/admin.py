from django.contrib import admin
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "publicada", "creada")
    list_filter = ("publicada", "creada")
    search_fields = ("titulo", "descripcion", "autor__username")
    readonly_fields = ("creada",)
