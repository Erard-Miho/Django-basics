from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.apps import apps

""" In the models.py section happens to create users """

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name 

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    """return string representaiton of the user"""
    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):
    """ Profile status update """
    """ These will help users to store status update of them ( history ) """
    """ We will link this model to other models and this is called a foreing KEY """
    """ This is decided by calling the usr profile from the setting to add it manually and the on_delete if the usr is deleted"""
    
    
    
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )

    

    status_text = models.CharField(max_length=255)
    # what was created
    created_on = models.DateTimeField(auto_now_add=True)
    # the date and time when created
    """ We add a model string """

    def __str__(self):
        """return the model as string"""
        return self.status_text
    


    