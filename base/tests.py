import ast
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from accounts.models import User


class BaseAPITestCase(APITestCase):

    def get_token(self, user):
        token = RefreshToken.for_user(user)
        return {
            "access": token.access_token,
        }

    def get_token_from_url(self, user, password):
        response = self.client.post(path=reverse('token_obtain_pair_api'),
                                    data={
                                        'username': user.username,
                                        "password": password
                                    }, format='json')
        return ast.literal_eval(response.content.decode("UTF-8"))

    def get_token_from_admin_user(self, phone="01983110845", password="1111"):
        user = User.objects.create_superuser(username=phone, password=password)
        return self.get_token_from_url(user, password)

    def get_token_from_user(self, phone="01983110842", password="1111"):
        user = User.objects.create_user(username=phone, password=password)
        return self.get_token_from_url(user, password)


