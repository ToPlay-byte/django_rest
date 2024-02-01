from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
    openapi.Info(
        title='API documentation',
        description='Here you can take information about our product',
        default_version='v1',
        contact=openapi.Contact(email='oleksandr.hnylosyr@gmail.com')
    ),
    public=True
)

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('api/catalog/', include('api.catalog.urls')),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/', include('drf_social_oauth2.urls')),
    path('shop/', include('frontend.settings.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
