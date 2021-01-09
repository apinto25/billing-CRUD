from django.urls import path, include
from rest_framework import routers

from apps.product.views.product_views import ProductViewsets


router = routers.DefaultRouter()
router.register(r'product', ProductViewsets)

urlpatterns = [path('', include(router.urls)), ]
