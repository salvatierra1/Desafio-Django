from apps import veterinaria
from django.urls import path
from apps.veterinaria.views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

app_name = "apps.veterinaria"

urlpatterns = [
    path('', ClienteListView.as_view(), name='listado_clientes'),
    path('nuevo', ClienteCreateView.as_view(), name='crear_clientes'),
    path('editar/<int:pk>', ClienteUpdateView.as_view(), name='editar_clientes'),
    path('eliminar/<int:pk>', ClienteDeleteView.as_view(), name='eliminar_clientes'),
]
