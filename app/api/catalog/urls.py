from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import ProductViewSet, CategoryViewSet


app_name = 'catalog'

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = router.urls
