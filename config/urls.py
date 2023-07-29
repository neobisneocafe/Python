from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin_panel/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/users/', include('users.urls')),
    path('api/barista/', include('barista.urls')),
    path('api/menu/', include('menu.urls')),
    path('api/stuff/'),include('stuff.urls'),
    path('api/warehouse/', include('warehouse.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
