from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FriendRequestsSerializer,PendingRequestSerializer, ARPstatusViewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import AllRequests
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle
# Create your views here.
class SendRequestView(APIView):
    http_method_names=['get','post']
    permission_classes=[IsAuthenticated]
    throttle_classes=[UserRateThrottle]
    def post(self,request):

        serializer=FriendRequestsSerializer(data=request.data,context={'request':request})
        if serializer.is_valid(raise_exception=True):
            newrequest= serializer.save(from_user=self.request.user)
            print("hh",self.request.user)
            return Response({'o/p':'friend Request sent'},status=status.HTTP_200_OK)
        return Response({'o/p':'destination user not found'},status=status.HTTP_400_BAD_REQUEST)

class PendingRequestView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=AllRequests.objects.all()
    serializer_class=PendingRequestSerializer
    http_method_names=['get']
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(to_user=self.request.user, status="Pending")
        return query_set

class ARPstatusView(viewsets.ModelViewSet):
    
    permission_classes=[IsAuthenticated]
    queryset=AllRequests.objects.all()
    serializer_class=ARPstatusViewSerializer
    http_method_names=['get','patch','put']
    # def get(self):
        
class MyFriendsView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=AllRequests.objects.all()
    serializer_class=ARPstatusViewSerializer
    http_method_names=['get']
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(to_user=self.request.user, status="Accepted")
        return query_set
    # def get(self):