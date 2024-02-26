from rest_framework import viewsets
from .serializer import RegionServerSerializer, RegionServerIPSerializer, RegionServerPortSerializer
from .models import RegionServer
from socket import *
from rest_framework.response import Response
from rest_framework.decorators import action
import psutil
import os

class RegionServerViewSet(viewsets.ModelViewSet):
    queryset = RegionServer.objects.all()
    serializer_class = RegionServerSerializer

    @action(detail=False, methods=['get'])
    def obtener_info_disco(self, request):
        try:
            # Obtener el PID del proceso actual
            pid = os.getpid()
            print("PID del proceso actual:", pid)
            
            # Obtener la información del disco
            info_disco = psutil.disk_usage("C:")
            
            # Convertir el espacio libre, utilizado y total a GB
            espacio_libre_gb = info_disco.free / (1024 * 1024 * 1024)
            espacio_utilizado_gb = info_disco.used / (1024 * 1024 * 1024)
            espacio_total_gb = info_disco.total / (1024 * 1024 * 1024)
            
            diskSpace = {
                "libre": espacio_libre_gb,
                "utilizado": espacio_utilizado_gb,
                "total": espacio_total_gb,
                "pid": pid
            }

            return Response(diskSpace)
        except Exception as e:
            print("Error al obtener información del disco:", e)
            return Response({"error": "Error al obtener información del disco"})
        
    def enviar_mensaje_socket(self, ip, puerto, libre, usado, total, pid):
        try:
            print("IP:", ip)
            print("Puerto:", puerto)
            print("Libre:", libre)
            print("Usado:", usado)
            print("Total:", total)
            print("PID:", pid)

            # Crear un socket y conectarlo al servidor receptor
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, puerto))

            # Formatear el mensaje
            mensaje = f"Libre: {libre}, Usado: {usado}, Total: {total}, PID: {pid}"
            
            # Enviar el mensaje
            sock.sendall(mensaje.encode())

            # Cerrar la conexión
            sock.close()
        except Exception as e:
            print("Error al enviar mensaje a través de socket:", e)

class RegionServerIPViewSet(viewsets.ModelViewSet):
    queryset = RegionServer.objects.all()
    serializer_class = RegionServerIPSerializer

class RegionServerPortViewSet(viewsets.ModelViewSet):
    queryset = RegionServer.objects.all()
    serializer_class = RegionServerPortSerializer


