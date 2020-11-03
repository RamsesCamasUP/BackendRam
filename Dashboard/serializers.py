from rest_framework import serializers
from .models import DashboardModel

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardModel
        fields =('nombre_com','edad','correo')