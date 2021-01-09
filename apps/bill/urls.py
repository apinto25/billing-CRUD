from django.urls import path, include
from rest_framework import routers

from apps.bill.views.bill_views import BillViewsets


router = routers.DefaultRouter()
router.register(r'bill', BillViewsets)

urlpatterns = [path('', include(router.urls)), ]
