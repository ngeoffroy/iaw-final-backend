from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from denuncias import views

# Api router
router = routers.DefaultRouter()
router.register('denuncias', views.DenunciaViewSet, basename='denuncias')
router.register('aprobadas', views.DenunciasAprobadasViewSet, basename='aprobadas')
router.register('pendientes', views.DenunciasPendientesViewSet, basename='pendientes')
router.register('revision', views.DenunciasEnRevisionViewSet, basename='revision')
router.register('terminadas', views.DenunciasTerminadasViewSet, basename='terminadas')

urlpatterns = [
    # Admin routes
    path('admin/', admin.site.urls),

    # Api routes
    path('', include('authentication.urls')),
    path('', include(router.urls)),
]

#Aviso a django que busque el directorio de images, porque sino no las trae
if settings.DEBUG:
    urlpatterns += static('/images/', document_root=settings.MEDIA_ROOT)