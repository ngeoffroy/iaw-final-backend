from rest_framework import viewsets
from .models import Denuncia
from .serializers import DenunciaSerializer


class DenunciaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer

class DenunciasAprobadasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Denuncia.objects.filter(autorizado=1, status=3).values()
    serializer_class = DenunciaSerializer

class DenunciasPendientesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Denuncia.objects.filter(status=0).values()
    serializer_class = DenunciaSerializer

class DenunciasEnRevisionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Denuncia.objects.filter(status=1).values()
    serializer_class = DenunciaSerializer

class DenunciasTerminadasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Denuncia.objects.filter(status=2).values()
    serializer_class = DenunciaSerializer