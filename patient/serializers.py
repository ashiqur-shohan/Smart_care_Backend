from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User




class PatientSerializers(serializers.ModelSerializer):
    # patient er sathe user er  relation ase .
    #by default ei relation ta rest api website a id diye dekhabe. ei change korar jonno nicher code likha
    #jehetu relation one to one tai many = false
    # user ta ke kivhabe dekhte chai sheita 
    # https://www.django-rest-framework.org/api-guide/relations/
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']
    #built - in function. jokhn user save korte jabe tokhn validate korbe. 
    def save(self):
        username = self.validated_data['username'] #cleaned_data er replace
        first_name = self.validated_data['first_name'] 
        last_name = self.validated_data['last_name'] 
        email = self.validated_data['email'] 
        password = self.validated_data['password'] 
        password2 = self.validated_data['confirm_password'] 

        if password !=password2:
            raise serializers.ValidationError({'error':'Password Does not match.'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':'Email already exists.'})
        account = User(username=username,email = email,first_name=first_name,last_name=last_name)
        account.set_password(password)
        #account acctive er bishoy ta off kore rakhtesi. email er link click korle tahole account create korte parbe.
        account.is_active = False
        account.save()
        return account
    

#login er jonno kono model drkr nai. 
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

