from rest_framework import serializers
from .models import Contact_us

#model ke json a convert kora hocche
# form er alternative. template niye kaj krle form use kora hoy.
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_us
        fields = '__all__'
