from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers, models
from rest_framework import viewsets
# We create the authentication
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
# Below we add the search option
from rest_framework import filters
# we create the auth TOKEN
from rest_framework.authtoken.views import ObtainAuthToken
# We import rest settings
from rest_framework.settings import api_settings

from rest_framework.permissions import IsAuthenticated
from django.shortcuts   import  render
from django.http import HttpResponse

# Create your views here.
class HelloApiView(APIView):
    """Test APIVIEW"""
    serializer_class=serializers.HelloSerializers

    def get(self,request,format=None):
        """Returns a list of apiview features"""
        an_apiview = [
            'Uses HTTP functions as (get,post,patch,put,delete)',
            'Is similar to a traditional django api view',
            'Gives you full control',
            'Is mapped automatically to URL',
        ]

        return Response({'message':'Hello There!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello msg with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Create put for updating a object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete a object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """created viewset class the viewsets.ViewSet is the viewset that rest_framework provide"""
    serializer_class = serializers.HelloSerializers
    def list(self,request):
        """Return a messsage"""
        a_viewsets= [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automaticlly provide to url using routing',
            'Provide more functionality using less code',
        ]

        return Response({'message':'Hello!','a_viewsets':a_viewsets})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting a object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self,request,pk=None):
        """Update a user"""
        return Response({'http_method':'PUT'})

    def patch(self,request,pk=None):
        """Handle updating a part of the user"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Destroy an object"""
        return Response({'http_method':'DELETE'})


""" For our api we gonna use a model viewset (like the simple viewset) to manage models for api"""
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle updating creating profiles"""
    """ And this is allowed by the viewsets.ModelViewSet """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # authentication made in tuple as cannot be changed
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,) # this will show to user if they have permission to change things
    # from the permission.py
    filter_backends = (filters.SearchFilter,)  
    """ DON'T FORGET THE COMMA SO PYTHON KNOW IT IS A TUPLE NOT A OBJECT """
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens. We have to set it manually with render_classes"""
    # We override it to make it visible for us 
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    # This will be enabled in the django admin 
    # And we add a url for this at urls.py

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, updating, reading profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer # pylint: disable=maybe-no-member
    queryset = models.ProfileFeedItem.objects.all() # pylint: disable=maybe-no-member
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


 
