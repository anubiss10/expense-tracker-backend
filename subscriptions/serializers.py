from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'name', 'cost', 'frequency', 'start_date', 'next_renewal_date']
        read_only_fields = ['next_renewal_date']

    def create(self, validated_data):
        return Subscription.objects.create(**validated_data)
