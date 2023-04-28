from django.urls import path
from cadastros import views
from .views import ObrasCreate
from .views import ObrasList,ObrasContato
from .views import ObrasUpdate,home


urlpatterns = [
    
    path('cadastrar/obras/', ObrasCreate.as_view(), name="cadastrar-Obra"),
    ########### listagem 
    path('listar/obras/', ObrasList.as_view(), name="listar-Obra"),
    path('listar/contatos/', ObrasContato.as_view(), name="listar-Contatos"),
    ########## editar
    path('editar/obras/<int:pk>/', ObrasUpdate.as_view(), name="editar-obra"),
    ########## CSV
    # path('export-csv/', views.export_csv, name='export-csv'),
]