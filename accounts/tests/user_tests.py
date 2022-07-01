from django.urls import reverse
from base.tests import BaseAPITestCase
from rest_framework import status
from accounts.models import User


class UsersTests(BaseAPITestCase):
    """
    It is used to test different types of units for a user that can be
    used to test individual units for the smallest verifiable part of a
    user such as a register, updating, partially updating, deleting,
    listing, and finding a user.

    To run this test case:
    python manage.py test accounts.tests.user_tests.UsersTests
    """

    def test_user_list(self):
        """
         Unit-testing to get list of users.
        """

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        response = self.client.get(path=reverse('create_list'))
        assert response.status_code == status.HTTP_200_OK

    def test_register_user(self):
        """
         Unit-testing to register a user.
        """

        data = {
            "first_name": "John",
            "last_name": "doe",
            "username": "01987564312",
            "balance_amount": "1000",
            "email": "john@gmail.com",
            "password": "1111"
        }
        response = self.client.post(path=reverse('create_list'), data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_user(self):
        """
         Unit-testing to fully update a user.
        """

        data = {
            "first_name": "John",
            "last_name": "doe",
            "username": "01987564312",
            "balance_amount": "1000",
            "email": "john@gmail.com",
            "password": "1111"
        }
        user = User.objects.create_user(username="01834129856", password="1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        response = self.client.put(path=reverse('user_retrieve_update_delete', kwargs={'pk': user.id}),
                                   data=data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_update_user_partially(self):
        """
         Unit-testing to partially update a user.
        """

        data = {
          "first_name": "justine",
          "last_name": "doe",
        }
        user = User.objects.create_user(username="01834129856", password="1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        response = self.client.patch(path=reverse('user_retrieve_update_delete', kwargs={'pk': user.id}),
                                     data=data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_get_user(self):
        """
         Unit-testing to get a user.
        """

        user = User.objects.create_user(username="01834129856", password="1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        response = self.client.get(path=reverse('user_retrieve_update_delete', kwargs={'pk': user.id}))
        assert response.status_code == status.HTTP_200_OK

    def test_delete_user(self):
        """
        User delete unit testing
        """

        user = User.objects.create_user(username="01834129856", password="1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        response = self.client.delete(path=reverse('user_retrieve_update_delete', kwargs={'pk': user.id}))
        assert response.status_code == status.HTTP_204_NO_CONTENT

