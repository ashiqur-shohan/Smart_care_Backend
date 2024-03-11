from rest_framework import serializers
from .models import Doctor,Specialization,Designation,AvailableTime,Review

class DoctorSerializers(serializers.ModelSerializer):
    # string use korle input dite pera hoy. dekhar jonno thik ache
    # user = serializers.StringRelatedField(many=False)
    # #ekhane relation many tai many = true kore diyechi
    # designation = serializers.StringRelatedField(many=True)
    # specialization = serializers.StringRelatedField(many=True)
    # available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = "__all__"


class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"


class AvailableTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = "__all__"


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"