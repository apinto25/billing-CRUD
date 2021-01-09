from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.bill.models.bill import Bill
from apps.bill.serializers.bill_serializer import BillSerializer


class BillViewsets(viewsets.GenericViewSet):
    queryset = Bill.objects.filter()

    def get_serializer_class(self):
        return BillSerializer
    
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
