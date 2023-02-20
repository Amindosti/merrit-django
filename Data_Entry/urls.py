from django.urls import include, path
from .views import CurrentUserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', CurrentUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]