from rest_framework import serializers
from .models import Appointment

#model ke json a convert kora hocche
# form er alternative. template niye kaj krle form use kora hoy.
class AppointmentSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many=False)
    patient = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = Appointment
        fields = '__all__'
