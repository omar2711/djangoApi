from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'regionserver', views.RegionServerViewSet)
router.register(r'ip', views.RegionServerIPViewSet)
router.register(r'port', views.RegionServerPortViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('diskSpace/', views.RegionServerViewSet.as_view({'get': 'obtener_info_disco'}), name='diskSpace'),
    path('sendMessage/', views.EnviarMensajeSocket.as_view(), name='sendMessage'),
    path('receiveMessage/', views.RecibirMensajeSocket.as_view(), name='receiveMessage'),
    path('sendInfoToDatabase/', views.EnviarInfoBaseDatos.as_view(), name='sendInfoToDatabase'),  # Agregar esta línea para el método POST
]

