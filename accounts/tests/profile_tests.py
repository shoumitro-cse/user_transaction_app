from django.urls import reverse
from base.tests import BaseAPITestCase
from rest_framework import status
from accounts.models import User


class UserProfileTests(BaseAPITestCase):
    """
    To run this test case:
    python manage.py test accounts.tests.profile_tests.UserProfileTests
    """

    def test_user_profile_create(self):
        data = {
          "bio": "developer",
          "dob": "2022-06-26",
          "address": "dhaka",
        }
        user = User.objects.create_user(username="01834129856", password="1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        response = self.client.post(path=reverse('profile_create'), data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_user_profile(self):
        data = {
          "bio": "developer",
          "dob": "2022-06-26",
          "address": "dhaka",
        }
        user = User.objects.create_user(username="01834129856", password="1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        response = self.client.put(path=reverse('user_profile_retrieve_update_delete'),
                                   data=data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_update_user_profile_partially(self):
        data = {
          "bio": "Teacher",
          "dob": "2022-06-29",
        }
        user = User.objects.create_user(username="01834129856", password="1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        response = self.client.patch(path=reverse('user_profile_retrieve_update_delete'),
                                     data=data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_get_user_profile(self):
        user = User.objects.create_user(username="01834129856", password="1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        response = self.client.get(path=reverse('user_profile_retrieve_update_delete'))
        assert response.status_code == status.HTTP_200_OK

    def test_delete_user_profile(self):
        user = User.objects.create_user(username="01834129856", password="1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_url(user, "1111").get("access")}')
        response = self.client.delete(path=reverse('user_profile_retrieve_update_delete'))
        assert response.status_code == status.HTTP_204_NO_CONTENT
