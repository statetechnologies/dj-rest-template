from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

from .admin import custom_admin_site

schema_view = get_schema_view(
    openapi.Info(
        title='DJ Template API',
        default_version='v1',
        description='DJ Template Backend API',
        contact=openapi.Contact(email='mrshanas.dev@gmail.com'),
        license=openapi.License(name='MIT')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)


urlpatterns = [
    path('dashboard/', custom_admin_site.urls),
    path('api/users/', include('users.urls')),

    # api docs
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # noqa
    path('schema', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
