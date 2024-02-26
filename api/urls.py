from django.urls import path, include
from rest_framework import routers
from api import views
from api.views import EnviarMensajeSocket

router = routers.DefaultRouter()
router.register(r'regionserver', views.RegionServerViewSet)
router.register(r'ip', views.RegionServerIPViewSet)
router.register(r'port', views.RegionServerPortViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('diskSpace/', views.RegionServerViewSet.as_view({'get': 'obtener_info_disco'}), name='diskSpace'),
    path('sendMessage/', EnviarMensajeSocket.as_view(), name='sendMessage'),

]
