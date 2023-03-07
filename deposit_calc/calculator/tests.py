from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import DepositView


class DepositTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_post_request(self):
        """Test status-code is OK"""

        request = self.factory.post(
            "/deposit",
            {"date": "31.01.2023", "periods": 15, "amount": 10_000, "rate": 6},
            format="json",
        )

        response = DepositView.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_empty_request(self):
        """Test empty request"""

        request = self.factory.post(
            "/deposit",
            {},
            format="json",
        )

        response = DepositView.as_view()(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.content,
            b"dateperiodsamountrate",
            "Empty request",
        )

    def test_incomplete_request(self):
        """Test incomplete request"""

        request = self.factory.post(
            "/deposit",
            {"date": "31.01.2023", "amount": 10_000, "rate": 6},
            format="json",
        )

        response = DepositView.as_view()(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.content,
            b"periods",
            "Incomplete request",
        )

    def test_unvalid_request(self):
        """Test unvalid request"""

        request = self.factory.post(
            "/deposit",
            {"date": "01.31.2023", "periods": 15, "amount": 10_000, "rate": 8},
            format="json",
        )

        response = DepositView.as_view()(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.content,
            b"date",
            "Unvalid request",
        )
