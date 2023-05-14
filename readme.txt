
-create signup api->
    In base app-
    view is UserSignUpview(APIView), and serializer is class UserSignUpviewSerializer
    add following fn in base.models.py to auto generate authtoken on saving the new user

-create login api->
    create userlogin view, add url path, get the posted data serialized in a obj by passing data in userlogin serializer class,
    if obj is valid, fetch email and password, authenticate(email, pass), if exist return login sucsess

-create Authtoken 'fetching' api=>
    In settings.py installed app
       add 'rest_framework.authtoken' 
       REST_FRAMEWORK={
        'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication']
       }
    In urls.py-
        from rest_framework.authtoken.views import obtain_auth_token
        then we will create a url path that will call 'obtain_auth_token' function to generate auth
    In views.py-
        add permission class IsAuthenticated in our requred view.
    now do makemigration- this will create a user_auth table in db

-create search user api->
    pip install django-filter, import Djangofilterbackend in views.py
    add pagination class in settings
    create SearchUser view, create SearchUserSerializer class, use viewser and pass the 
    import basicauthentication for search view

The model AllRequests format is-

    # req id        from user id   to user id    pending(Def-True)     status(Def-NR)
    #   xyz12           3             1           False                 Accepted
    #   adn23           3             2           True                    NR
    #   wlf45           1             3           False                 Rejected
    
-create api to friend request send->
    It's a post request, authenticated user will give the- to_user id and the request will be created
        in All request model, set unique_together = ['from_user','to_user'] to avoid same friend requests
        add userrate throttle class in views, and default throttle rates=3/min in settings.py
-create api to friend request accept/reject->first hit get, then take the request_id from o/p Json
    enter the request id value at url end, change request to patch, in body add {"status": "Accepted"}
-create api to list 'my' pending requests->
    used modelviewser-> get allrequests from  AllRequest model in queryset and filter queryset with--
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(to_user=self.request.user, status="Pending")
        return query_set
        or we can remove pending field from model and fetch requests with status=NR
    restrict the methods allowed to ['get']

-create api to list 'My friends' (accepted)->
    simillary filter query set with status=accepted

TokenBasedAuthentication-
Generating Authtoken-
    In settings.py installed app
       add 'rest_framework.authtoken' 

       REST_FRAMEWORK={
        'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication']
       }
    In urls.py-
        from rest_framework.authtoken.views import obtain_auth_token
        then we will create a url path that will call 'obtain_auth_token' function to return auth
    In views.py-
        add permission class IsAuthenticated in our requred view.
    now do makemigration- this will create a user_auth table in db
    
qsn - why need to again define field before Meta class in Serializers

