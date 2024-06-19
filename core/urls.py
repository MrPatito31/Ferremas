from django.urls import path
from .views import *

urlpatterns = [
    path('', catalogo, name='catalogo'),
    path('login', registro_login_view, name='registro_login'),
    path('', inicio_view, name='inicio'),  # Vista de inicio para redirección después del login/registro
    path('logout', logout, name="logout"),
    path('administrador', administrador),
    path('pago_view', pago_view, name="pago_view"),
    path('bodega', bodega, name="bodega"),
    path('addtocar/<codigo>', addtocar, name="addtocar"),
    path('dropitem/<codigo>', dropitem, name="dropitem"),
    path('pago/', pago, name='pago'),
    path('execute/', execute, name='execute'),
    path('comprar/', comprar, name='comprar'),
    path('historial', historial, name="historial"),
]   