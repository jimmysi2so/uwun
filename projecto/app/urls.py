from django.urls import path
from .views import home, contacto, verproducto, productos

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('verproducto/', verproducto, name="verproducto"),
    path('productos/', productos, name="productos"),
]
