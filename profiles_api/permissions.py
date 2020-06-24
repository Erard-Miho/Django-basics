""" We create permissions to modify users api/1,2,3... """ 
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit (GET,UPDATE,...) """
        """ But only to their profile and can view others with GET"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id 
"""This will return their profile or false if they're trying for others """


class UpdateOwnStatus(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id