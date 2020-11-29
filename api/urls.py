from django.conf.urls import url
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework.permissions import AllowAny

from .views.products import ProductViewSet
app_name = 'api'


router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1',
        description='API',
    ),
    permission_classes=(AllowAny,),
    urlconf='api.urls',
)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0,), name='schema-swagger-ui')
]
