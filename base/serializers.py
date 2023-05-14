from rest_framework import serializers
from base.models import SMUser

class UserSignUpviewSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'},write_only=True) #we added password2 because in...
    class Meta:
        model = SMUser
        fields = ['email','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }
#write_only. Set this to True to ensure that the field may be used 
# when updating or creating an instance, but is not included when serializing the representation
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password!=password2:
            raise serializers.ValidationError("Password do not match with confirm pass")
        #return super().validate(attrs)
        return attrs
    
    def create(self, validate_data):
        return SMUser.objects.create_user(**validate_data)
    # we redefined create fn bcz we are using customized User model

class UserLoginviewSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = SMUser
        fields='__all__'

class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMUser
        fields= ['email']