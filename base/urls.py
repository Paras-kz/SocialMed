
from django.urls import path,include
from base.views import UserSignUpview,UserLoginview,SearchUserview
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register('search',SearchUserview)

urlpatterns = [
    path('signup/',UserSignUpview.as_view(), name='signUp'),
    path('login/',UserLoginview.as_view(), name='login'),
    path('', include(router.urls)),
    path('get-auth/',obtain_auth_token,name="myuser_auth"),
]
#url-  http://127.0.0.1:8000/api/user/