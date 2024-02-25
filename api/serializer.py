from rest_framework import serializers

from .models import RegionServer

class RegionServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionServer
        fields = '__all__'