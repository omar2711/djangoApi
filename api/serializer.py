from rest_framework import serializers

from .models import RegionServer

class RegionServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionServer
        fields = '__all__'

class RegionServerIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionServer
        fields = ['ip', 'pid']

class RegionServerPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionServer
        fields = ['port', 'pid']
