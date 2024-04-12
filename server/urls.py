from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from denuncias import views

# Api router
router = routers.DefaultRouter()
router.register('denuncias', views.DenunciaViewSet, basename='denuncias')
router.register('changestatus', views.ChangeStatusViewSet, basename='changestatus')
router.register('changeautorizado', views.ChangeAutorizadoViewSet, basename='changeautorizado')

urlpatterns = [
    # Admin routes
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('', include(router.urls)),
]

#Aviso a django que busque el directorio de images, porque sino no las trae
if settings.DEBUG:
    urlpatterns += static('/images/', document_root=settings.MEDIA_ROOT)