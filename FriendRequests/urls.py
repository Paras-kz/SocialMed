from django.urls import path,include
from .views import SendRequestView,PendingRequestView,ARPstatusView,MyFriendsView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register('pending-req',PendingRequestView) 
router.register('ARPstatus',ARPstatusView)
router.register('My-friends',MyFriendsView)

urlpatterns = [
    path('sendRequest/',SendRequestView.as_view(), name='send-request'),
    path('', include(router.urls)),

]

#url-  http://127.0.0.1:8000/api/Requests/