from django.contrib import admin
from django.urls import path
from . import serializers
from . import views
from .views import register_user, PersonaList


urlpatterns = [
    
    
    path('zapatilla/', views.ZapatillaList.as_view()),
    path('zapatilladetalle/<int:pk>', views.ZapatillaDetail.as_view()),
    path('zapatilladelete/<int:pk>', views.ZapatillaDelete.as_view()),
    path('persona/', views.PersonaList.as_view()),
    path('personadetalle/<int:pk>', views.PersonaDetail.as_view()),
    path('personadelete/<int:pk>', views.PersonaDelete.as_view()),
    path('register/', register_user, name='register_user'),



    
]

