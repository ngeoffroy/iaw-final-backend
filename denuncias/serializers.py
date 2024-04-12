from rest_framework import serializers
from .models import Denuncia

class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = '__all__'

class DenunciaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = '__all__'

class DenunciaAutorizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = 'id', 'autorizado'