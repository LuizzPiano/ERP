from django.contrib import admin
from .models import Obras,Contatos

# admin.site.register(Obras)
@admin.register(Obras)
class ObrasAdmin(admin.ModelAdmin):
    search_fields = ('DC','status','status_final','Colaborador_1','Colaborador_2','Obs','Data_01','Data_02')
    list_display = ('DC','status','status_final','Colaborador_1','Colaborador_2','Obs','Data_01','Data_02')
    list_filter = ('status','status_final','Colaborador_1','Colaborador_2','Data_01','Data_02')
    




@admin.register(Contatos)
class ContatosAdmin(admin.ModelAdmin):
    list_display = ('Nome','Area','Funcao')