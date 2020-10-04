from rest_framework import serializers
from swap_analysis.apps.swap.models import Swap
from swap_analysis.apps.swap.models import Attendant
from datetime import datetime


class SwapSerializer(serializers.ModelSerializer):
    attendant = serializers.PrimaryKeyRelatedField(
        queryset=Attendant.objects.all(), required=False)
    driven_distance = serializers.FloatField(min_value=0)
    out_state_of_charge = serializers.FloatField(min_value=0)
    used_energy = serializers.FloatField(min_value=0)

    class Meta:
        model = Swap
        fields = ['id', 'battery_in', 'battery_out', 'station', 'driven_distance',
                  'out_state_of_charge', 'in_state_of_charge', 'attendant', 'used_energy', 'created_at']


class StatSerializer(serializers.Serializer):
    date = serializers.DateField(required=False, default=datetime.now().date)
    # total_energy_used = serializers.FloatField(required=False)
