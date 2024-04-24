from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from magicapi.models import *
from magicapi.views import *


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"users", Users, "user")
router.register(r"participants", Participants, "participant")
router.register(r"services", Services, "service")
router.register(r"magicianservices", MagicianServices, "magicianservice")

urlpatterns = [
    path('', include(router.urls)),
]

