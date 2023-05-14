from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from base.serializers import UserSignUpviewSerializer, UserLoginviewSerializer, SearchUserSerializer
from django.contrib.auth import authenticate
from rest_framework import viewsets
from base.models import SMUser
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserSignUpview(APIView):
    def post(self,request):
        serializer = UserSignUpviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            newuser = serializer.save()
            return Response({'o/p':'user created'},status=status.HTTP_201_CREATED)
        return Response({'o/p':'user not created'},status=status.HTTP_400_BAD_REQUEST)
class UserLoginview(APIView):
    def post(self, request):
        serializer=UserLoginviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            #check=SMUser.objects.filter(email=request.data['email'],password=request.data['password'])
            #if check is not None: login..?
            email=serializer.data.get('email')
            password= serializer.data.get('password')
            user=authenticate(email=email, password=password)# it will check in db if any user with these credentials exist
            if user is not None:
                return Response({'o/p':'login successful'},status=status.HTTP_200_OK)
            else:
                return Response({'o/p':'invalid login'},status=status.HTTP_400_BAD_REQUEST)

class SearchUserview(viewsets.ModelViewSet):
    # SMUser.objects.filter(email__istartswith='x') ->using lookups
    #authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=SMUser.objects.all()
    serializer_class=SearchUserSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['^email']

