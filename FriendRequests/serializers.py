from rest_framework import serializers
from base.models import SMUser
from .models import AllRequests

class FriendRequestsSerializer(serializers.ModelSerializer):
    # from_user=serializers.SerializerMethodField('_user')

    # def _user(self,obj):
    #     request =self.context.get('request',None)
    #     if request:
    #         return request.user
    # from_user = serializers.SerializerMethodField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model=AllRequests
        fields=['to_user']
    # def validate(self,data):
    #     #r=AllRequests.objects.get(from_user=self.context["request"].user,to_user=data['to_user'])
    #     # print(r,data)
    #     print("asfg",self.context["request"].__dict__,data['to_user'])
    #     # k=self.context["request"].id==data['to_user']
    #     # if k is True:
    #     #     k=None
    #     # if r is not None:
    #     #     raise serializers.ValidationError("request already present")
    #     # # elif self.context["request"]==data['to_user']:
    #     # #     raise serializers.ValidationError("can not send request to self")
    #     return data
        
        
    # def validate(self,data):
    #     if self.context["request"].user!=data['to_user']:
    #         return data

class PendingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=AllRequests
        fields='__all__'
    
class ARPstatusViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=AllRequests
        # fields=['from_user','status']
        fields='__all__'

    def validate(self,data):
        r=AllRequests.objects.get(to_user=self.context["request"].user,from_user=data['from_user'])
        if r is not None:
            print(data)
            return data
    # def validate(self, data):
    #     # print(data['request_id'])
    #     # print(self.context["request"].user)
    #     r=AllRequests.objects.get(request_id=data['request_id'])
    #     if r.to_user == self.context["request"].user:
    #     #if r.to_user == self.request.user:
    #         return data