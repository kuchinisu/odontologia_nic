from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),

    path('admin/', admin.site.urls),

    path('api/registros/', include('apps.registros_de_pacientes.urls')),
    path('api/identificacion/', include('apps.identificacion.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
