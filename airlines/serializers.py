from rest_framework import serializers
from .models import Testplane

class TestplaneSerializer(serializers.ModelSerializer):
    fuel_consumption_per_minute = serializers.ReadOnlyField()
    max_flying_minutes = serializers.ReadOnlyField()
    
    class Meta:
        model = Testplane
        fields = '__all__'
