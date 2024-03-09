from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from denuncias.models import Denuncia


"""
@author ngeoffroy
Activo la gestión de usuarios desde el panel de administración
"""
@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass

"""
@author ngeoffroy
Activo la gestión de denuncias desde el panel de administración
"""
@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    pass