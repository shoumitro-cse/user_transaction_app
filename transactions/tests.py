from django.urls import reverse

from accounts.models import User
from base.tests import BaseAPITestCase
from rest_framework import status
from transactions.models import Transactions


class TransactionsTests(BaseAPITestCase):

    """
    To run this test case:
    python manage.py test transactions.tests.TransactionsTests
    """

    def test_get_transaction_list(self):
        """
         Unit-testing to get list of transactions.
        """

        user = User.objects.create_user(username="01834129856", password="1111", balance_amount=1000)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        response = self.client.get(path=reverse('transaction_create_list'))
        assert response.status_code == status.HTTP_200_OK

    def test_create_transaction(self):
        """
         Unit-testing to create a user transaction.
        """

        sender_user = User.objects.create_user(username="01834129856", password="1111", balance_amount=1000)
        receiver_user = User.objects.create_user(username="01834129857", password="1111", balance_amount=1000)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(sender_user, "1111").get("access")}')
        transaction_data = {
            "scheduled_date_time": "2022-07-01T18:26:22.683899+06:00",
            "amount": "100",
            "receiver_user": receiver_user.id
        }
        response = self.client.post(path=reverse('transaction_create_list'),
                                    data=transaction_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_transaction(self):
        """
         Unit-testing to fully update a single transaction.
        """

        user = User.objects.create_user(username="01834129856", password="1111", balance_amount=1000)
        receiver_user = User.objects.create_user(username="01834129857", password="1111", balance_amount=1000)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        transaction = Transactions.objects.create(sender_user=user, receiver_user=receiver_user, amount=10)
        transaction_data = {
            "amount": "20",
            "receiver_user": receiver_user.id
        }
        response = self.client.put(path=reverse('transaction_retrieve_update_delete', kwargs={'pk': transaction.id}),
                                   data=transaction_data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_update_transaction_partially(self):
        """
         Unit-testing to partially update a single transaction.
        """

        user = User.objects.create_user(username="01834129851", password="1111", balance_amount=1000)
        receiver_user = User.objects.create_user(username="01834129857", password="1111", balance_amount=1000)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        transaction = Transactions.objects.create(sender_user=user, receiver_user=receiver_user, amount=10)
        transaction_data = {
            "amount": "10",
        }
        response = self.client.patch(path=reverse('transaction_retrieve_update_delete', kwargs={'pk': transaction.id}),
                                     data=transaction_data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_get_transaction(self):
        """
         Unit-testing to get a single transaction.
        """

        user = User.objects.create_user(username="01834129859", password="1111", balance_amount=1000)
        receiver_user = User.objects.create_user(username="01834129857", password="1111", balance_amount=1000)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        transaction = Transactions.objects.create(sender_user=user, receiver_user=receiver_user, amount=10)
        response = self.client.get(path=reverse('transaction_retrieve_update_delete', kwargs={'pk': transaction.id}))
        assert response.status_code == status.HTTP_200_OK

    def test_delete_transaction(self):
        """
        Transaction delete unit testing
        """

        user = User.objects.create_user(username="01834129857", password="1111", balance_amount=1000)
        receiver_user = User.objects.create_user(username="01834129857", password="1111", balance_amount=1000)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        transaction = Transactions.objects.create(sender_user=user, receiver_user=receiver_user, amount=10)
        response = self.client.delete(path=reverse('transaction_retrieve_update_delete', kwargs={'pk': transaction.id}))
        assert response.status_code == status.HTTP_204_NO_CONTENT
