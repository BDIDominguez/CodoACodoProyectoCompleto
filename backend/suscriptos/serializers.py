from rest_framework import serializers
from .models import Suscripto

class SuscriptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripto
        fields = ['id', 'email', 'date_subscribed']
