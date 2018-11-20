from rest_framework import serializers
from .models import Ride


class RideSerializer(serializers.Serializer):
    origin = serializers.CharField(max_length=255)
    destination = serializers.CharField(max_length=255)
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()
    passengers = serializers.IntegerField()
    driver_id = serializers.IntegerField()

    def create(self, validated_data):
        return Ride.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.origin = validated_data.get('origin', instance.origin)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.date = validated_data.get('date', instance.date)
        instance.passengers = validated_data.get('passengers', instance.passengers)
        instance.driver_id = validated_data.get('driver_id', instance.driver_id)

        instance.save()
        return instance