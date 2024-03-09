from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import UserSerializer
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

# Create your views here.

"""
@author ngeoffroy
Vista que captura los parámetros necesarios para el inicio de sesión
"""

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        psw = request.data.get('password', None)

        user = authenticate(email=email, password=psw)

        if not user==None:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        else:
             return Response(UserSerializer(user).data, status=status.HTTP_401_UNAUTHORIZED)
    

"""
@author ngeoffroy
Vista que realiza el cierre de sesión de un usuario
"""

class LogoutView(APIView):

     def post(self, request):
          logout(request)
          return Response(status=status.HTTP_200_OK)

"""
@author ngeoffroy
Vista que registra un usuario. 
Utilizo una vista otorgada por DRF para el armado de usuarios
"""

class CreateNewUserView(generics.CreateAPIView):
     serializer_class = UserSerializer


"""
@author ngeoffroy
Recupero el token generado para enviar el mail de reseteo de contraseña
"""

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Aquí deberíamos mandar un correo al cliente...
    print("Recupera la contraseña del correo '{reset_password_token.user.email}' usando el token '{reset_password_token.key}' desde la API http://localhost:8000/reset/confirm/.")