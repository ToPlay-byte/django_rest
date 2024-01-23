from rest_framework.routers import DefaultRouter, format_suffix_patterns

from django.urls import path

from .views import ProductViewSet, CategoryViewSet, WishListUserViewSet


app_name = 'catalog'

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

wish_list = WishListUserViewSet.as_view({
    'get': 'list'
})

wish_detail = WishListUserViewSet.as_view({
    'delete': 'destroy',
    'post': 'create'
})

urlpatterns = format_suffix_patterns([
    path('wish/', wish_list, name='wish-list'),
    path('wish/<int:pk>', wish_detail, name='wish-detail')
])

urlpatterns += router.urls
