from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuscriptoViewSet

router = DefaultRouter()
router.register(r'suscriptos', SuscriptoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
