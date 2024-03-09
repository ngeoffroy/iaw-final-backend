from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
#importo un generador de psw

"""
@author ngeoffroy
Serializo el modelo de user
"""

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model=get_user_model()
        fields = ('email', 'username', 'password')

        validate_password = make_password