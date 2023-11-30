from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import ProductViewSet


app_name = 'catalog'

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = router.urls
