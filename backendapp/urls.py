from django.urls import path, include
from rest_framework import routers
from .views import ApplicationViewSet

router = routers.DefaultRouter()
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
