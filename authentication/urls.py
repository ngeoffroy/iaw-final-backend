from django.urls import path, include
from .views import LoginView, LogoutView, CreateNewUserView
"""
@author ngeoffroy
Archivo para guardar las urls del módulo de authentication 
"""

urlpatterns = [
    # Auth views
    path('login/',
         LoginView.as_view(), name='login'),

    path('logout/',
         LogoutView.as_view(), name='logout'),

    path('create/',
         CreateNewUserView.as_view(), name='createnewuser'),

    path('resetpassword/',
         include('django_rest_passwordreset.urls'), name='resetpassword'),
]