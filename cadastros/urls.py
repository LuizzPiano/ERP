from django.urls import path

from .views import ObrasCreate
from .views import ObrasList
from .views import ObrasUpdate


urlpatterns = [
    path('cadastrar/obras/', ObrasCreate.as_view(), name="cadastrar-Obra"),



        #listagem 
    path('listar/obras/', ObrasList.as_view(), name="listar-Obra"),



    ########## editar

    path('editar/obras/<int:pk>/', ObrasUpdate.as_view(), name="editar-obra"),
]