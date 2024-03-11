from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewset, UserViewset


router = DefaultRouter()
# Posts routes
router.register(r"posts", PostViewset, basename="post")
# User routes
router.register(r"user", UserViewset, basename="user")
urlpatterns = router.urls
