from rest_framework import viewsets
from .serializer import RegionServerSerializer, RegionServerIPSerializer, RegionServerPortSerializer
from .models import RegionServer
from socket import *
from rest_framework.response import Response
from rest_framework.decorators import action
import psutil
import os
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import socket as sock_module


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
        


class EnviarMensajeSocket(APIView):
    def get(self, request):
        ip = request.GET.get('ip')
        puerto = request.GET.get('puerto')
        libre = request.GET.get('libre')
        usado = request.GET.get('usado')
        total = request.GET.get('total')
        pid = request.GET.get('pid')

        try:
            # Crear un socket y conectarlo al servidor receptor
            sock = sock_module.socket(sock_module.AF_INET, sock_module.SOCK_STREAM)
            sock.connect((ip, int(puerto)))  # Asegúrate de convertir el puerto a entero

            # Formatear el mensaje
            mensaje = f"Libre: {libre}, Usado: {usado}, Total: {total}, PID: {pid}"
            
            # Enviar el mensaje
            sock.sendall(mensaje.encode())

            # Cerrar la conexión
            sock.close()

            return Response({'success': True}, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error al enviar mensaje a través de socket:", e)
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RecibirMensajeSocket(APIView):
    def get(self, request):
        try:
            # Crear un socket y escuchar conexiones
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_sock.bind(("0.0.0.0", 69))  # Escuchar en todas las interfaces en el puerto 9000
            server_sock.listen(1)

            # Aceptar la conexión entrante
            client_sock, addr = server_sock.accept()

            # Recibir el mensaje
            mensaje_recibido = client_sock.recv(1024)
            mensaje_recibido_decodificado = mensaje_recibido.decode()

            # Cerrar la conexión
            client_sock.close()
            server_sock.close()

            return Response({'mensaje_recibido': mensaje_recibido_decodificado}, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error al recibir mensaje a través de socket:", e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class RegionServerIPViewSet(viewsets.ModelViewSet):
    queryset = RegionServer.objects.all()
    serializer_class = RegionServerIPSerializer

class RegionServerPortViewSet(viewsets.ModelViewSet):
    queryset = RegionServer.objects.all()
    serializer_class = RegionServerPortSerializer


