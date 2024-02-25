from rest_framework import viewsets
from .serializer import RegionServerSerializer
from .models import RegionServer

class RegionServerViewSet(viewsets.ModelViewSet):
    queryset = RegionServer.objects.all()
    serializer_class = RegionServerSerializer