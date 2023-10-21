from unittest.mock import patch, Mock

from django.test import TestCase
from django.urls import reverse

from .views import payment_process, payment_completed, payment_canceled


class PaymentProcessTests(TestCase):
    @patch("stripe.checkout.Session.create")
    def test_payment_process_view(self, stripe_mock):
        # Simular petición POST
        self.client.post(reverse("payment:process"), {})

        # Verificar llamada a API de stripe
        self.assertTrue(stripe_mock.called)

        # Verificar parámetros de sesión
        expected_session_args = {
            "mode": "payment",
            "client_reference_id": "order-id",
            "success_url": "http://success",
            "cancel_url": "http://cancel",
            "line_items": [...],
        }
        stripe_mock.assert_called_with(**expected_session_args)

        # Verificar redirección a URL de checkout
        stripe_session = stripe_mock.return_value
        stripe_session.url = "http://stripe-redirect"
        response = self.client.post(reverse("payment:process"))
        self.assertRedirects(response, stripe_session.url, status_code=303)


class PaymentCompletedTests(TestCase):
    def test_payment_completed_view(self):
        response = self.client.get(reverse("payment:completed"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "payment/completed.html")


class PaymentCanceledTests(TestCase):
    def test_payment_canceled_view(self):
        response = self.client.get(reverse("payment:canceled"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "payment/canceled.html")
