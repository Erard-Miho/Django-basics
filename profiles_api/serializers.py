from rest_framework import serializers
from profiles_api import models

class HelloSerializers(serializers.Serializer):
    """Serializes a name field for our apiview"""
    name = serializers.CharField(max_length=10)

"""-------Serialize a user profile object-------"""

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        """ We create new models in models.py using our serializer """
        fields = ('id', 'email', 'name', 'password')
        """ Below we add info about what you need to write """
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style':{'input_type':'password'}
            }
        }
        """ By default the serializer allows to create simple object in the database uses the default 
        function of the object manager. So we want to override this functionality to make the create
        user function instead of create function. We do this to HASH the password. """
    def create(self, validated_data):
        """ create and return a new user """
        """ This will override the Userprofile function and call create_user in models.py """
        """ SET method """
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        """ Get method """
        return user


""" The serializer for the feeditem"""
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed item"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile':{'read_only':True}
        }