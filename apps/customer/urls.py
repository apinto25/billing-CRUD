from django.urls import path, include
from rest_framework import routers

from apps.customer.views.customer_views import CustomerViewsets


router = routers.DefaultRouter()
router.register(r'customer', CustomerViewsets)

urlpatterns = [path('', include(router.urls)), ]
