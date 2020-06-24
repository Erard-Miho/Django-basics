from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet) 
router.register('feed', views.UserProfileFeedViewSet)

""" we dont need basename because we have queryset
which finds name by itself. Or if we want to override the queryset we add a basename"""

urlpatterns = [
    path('Hello-view',views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    #path('', include(router.urls)) 

   
]
