from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from core.views import RegistrationAPIView, LoginAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Polls API",
      default_version='v1',
      description="description",
      contact=openapi.Contact(email="alex@rocketcompute.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('polls.urls')),
    path('auth/login/', LoginAPIView.as_view()),
    path('auth/register/', RegistrationAPIView.as_view()),

    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

