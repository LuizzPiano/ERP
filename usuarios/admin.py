from django.contrib import admin
from .models import Perfil

# Register your models here.
# admin.site.register(Perfil)
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome_completo','ind','telefone','veiculo','Cor','Placa','Tipo_veiculo')