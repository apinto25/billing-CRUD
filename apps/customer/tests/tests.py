from django.test import TransactionTestCase, Client
from rest_framework import status

from apps.customer.models.customer import Customer
from apps.customer.serializers.customer_serializer import CustomerSerializer

client = Client()


class CustomerTest(TransactionTestCase):
    reset_sequences = True

    def test_list_questions(self):
        """Test list customers."""

        response = client.get(
            "/customer/",
            content_type="application/json"
        )
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
