from django.contrib import admin
from .models import (
    Colaboradores,
    Base, 
    Folga, 
    Escala
)


class EscalaAdmin(admin.ModelAdmin):
    list_display = ('colaborador','data','disponivel')


admin.site.register(Colaboradores)
admin.site.register(Base)
admin.site.register(Folga)
admin.site.register(Escala, EscalaAdmin)