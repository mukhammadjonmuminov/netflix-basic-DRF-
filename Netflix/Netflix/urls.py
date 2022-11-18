from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
   openapi.Info(
      title="Netflix Application APi",
      default_version="v1",
      description="Swager docs for REST API",
      contact=openapi.Contact("Mukhammadjon Muminov <gmail@muhammadjonmominov77.com>")
   ),
   public=True,
   permission_classes=[AllowAny, ]
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('home.urls')),
   path('docs/', schema_view.with_ui('swagger'), name="swagger-docs"),
   path('redoc/', schema_view.with_ui('redoc'), name="redoc"),
]
