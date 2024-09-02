from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from books import views # book management system

#  API REST framework router
router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

# schema_view for Swagger
schema_view = get_schema_view(
    openapi.Info(
      title="Book Management API",
      default_version='v1',
      description=(
            "Welcome to the Book Management API documentation! This API provides a comprehensive suite of endpoints to manage your book collection seamlessly. "
            "Whether you're looking to add new books, update existing records, or retrieve detailed information about specific titles, our API is designed to make book management simple and efficient. "
            "Explore the various features and capabilities of the API to optimize your book-related tasks and integrate effortlessly into your existing systems."
      ),
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="heroeskq3@gmail.com"),
      license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls), #admin
    path('api/', include(router.urls)),  # API routes
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Para Swagger UI
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-swagger-yaml'),  # Para descargar el archivo YAML
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Para ReDoc
]
