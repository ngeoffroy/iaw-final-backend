from rest_framework import viewsets
from .models import Denuncia
from .serializers import DenunciaSerializer, DenunciaStatusSerializer
from rest_framework import status
from rest_framework.response import Response
import io, os
from google.cloud import vision
from google.cloud.vision_v1 import types
from rest_framework.response import Response
from rest_framework import status
from .serializers import DenunciaSerializer

PALABRAS_NO_TOLERADAS = {
    "nivel1": ['tonto','feo'],
    "nivel2": ['horrible', 'newbie'],
    "nivel3": ['manco']
}
PENALIDADES = {
    "nivel1":10,
    "nivel2":30,
    "nivel3":60
}

class DenunciaViewSet(viewsets.ViewSet):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'lexical-pattern-419622-3d30590cc140.json' #Vinculo mi clave con las credenciales de google
    def list(self, request):
        queryset = Denuncia.objects.all()
        serializer_class = DenunciaSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    
    def retreive(self, request, pk=None):
        id=pk
        if id is not None:
            denuncia=Denuncia.objects.get(id=id)
            serializer=DenunciaSerializer(denuncia)
            return Response(serializer.data)
        
    def create(self,request):

        serializer=DenunciaSerializer(data=request.data)
        if serializer.is_valid():
            imagen = request.data['imagen']
            texto = self.extraer_texto(imagen)
            rtdo, pena = self.analizar_texto(texto)
            if rtdo:
                serializer.validated_data['status'] = 2
                serializer.validated_data['pena'] = pena
            else:
                serializer.validated_data['status'] = 1
            serializer.save()
            return Response({'msg':'Denuncia registrada'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def extraer_texto(self, imagen_data):
        client = vision.ImageAnnotatorClient() #cliente de google cloud
        imagen = types.Image(content=imagen_data.read()) #prepara la imagen para ser extraida
        response = client.text_detection(image=imagen)
        texts = response.text_annotations #extraigo la info junto a otros parametros como las coordenadas
        print(texts)
        texto_extraido = [text.description for text in texts]
        return texto_extraido
    
    def analizar_texto(self, texts):
        pena = 0
        encontre = False
        print(texts)
        for text in texts:
            for nivel, palabra in PALABRAS_NO_TOLERADAS.items():
                if text in palabra:
                    encontre = True
                    pena = max(PENALIDADES[nivel], pena) #Me quedo con la maxima pena en caso de tener varios insultos en una misma imagen
        return encontre, pena

    
    def destroy(self, request,pk):
        id=pk
        stu=Denuncia.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Denuncia eliminada'}, status.HTTP_200_OK)

class ChangeStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaStatusSerializer

    def post(self, request):
        id = request.query_params.get('id')
        nuevo_status = request.query_params.get('status')

        if id:
            denuncia = Denuncia.objects.filter(id=id).first()
            if denuncia:
                denuncia.status = nuevo_status
                denuncia.save()
                serializer = self.serializer_class(denuncia)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Denuncia no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Se requiere el parámetro "id"'}, status=status.HTTP_400_BAD_REQUEST)

class ChangeAutorizadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaStatusSerializer

    def post(self, request):
        id = request.query_params.get('id')
        nuevo_autorizado = request.query_params.get('autorizado')

        if id:
            denuncia = Denuncia.objects.filter(id=id).first()
            if denuncia:
                denuncia.autorizado = nuevo_autorizado
                denuncia.save()
                serializer = self.serializer_class(denuncia)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Denuncia no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Se requiere el parámetro "id"'}, status=status.HTTP_400_BAD_REQUEST)
