
from django.contrib import admin
# adicionar o include para importar urls dos apps
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),
    path('', include('usuarios.urls')),
    path('', include('cadastros.urls')),
    path('', include('escalas.urls')),
    

] 

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)