from django.urls import path
from .views import (
    home,
    lista_Colaboradores,
    Colaboradores_novo,
    Colaboradores_update,
    lista_bases,
    bases_novo,
    bases_update,
    lista_escalas,
    escala_novo,
    escala_update,
    escala_delete,
    lista_folgas,
    folga_novo,
    folga_update,
    folga_delete,
    EscolaCreate,
    EscalaList,
    
    
)



urlpatterns = [
    path('ss', home, name='cadastro_home'),
    path('colaboradores', lista_Colaboradores, name='lista_colaboradores'),
    # path('colaboradores-novo', Colaboradores_novo, name='colaboradores_novo'),
    # path('colaboradores-update/<int:id>/', Colaboradores_update, name='colaboradores_update'),
    
    # path('bases', lista_bases, name='lista_bases'),
    # path('bases_novo', bases_novo, name='bases_novo'),
    # path('bases-update/<int:id>/', bases_update, name='bases_update'),

    path('escalas-listas', EscalaList.as_view(), name='lista_escalas'), 
    path('escalas-creat', EscolaCreate.as_view(), name='escala-creat'), 
    path('escala-novo', escala_novo, name='core_escala_novo'),
    path('escala-update/<int:id>/', escala_update, name='core_escala_update'),
    path('escala-delete/<int:id>/', escala_delete, name='core_escala_delete'),
    # path('relatorio-pdf/', PdfEscalas.as_view(),name='relatorio_pdf_escalas'),

    # path('folgas', lista_folgas, name='core_lista_folgas'),
    # path('folga-novo', folga_novo, name='core_folga_novo'),
    # path('folga-update/<int:id>/', folga_update, name='core_folga_update'),
    # path('folga-delete/<int:id>/', folga_delete, name='core_folga_delete'),
]
