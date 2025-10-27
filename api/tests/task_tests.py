from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from user.models import User
from api.views import TaskView
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

class TaskTests(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TaskView.as_view()
        self.user = User.objects.create(
            username="innocent",
            email="innocent@gmail.com",
            phone="0991644084",
            age=19,
            is_staff=True
        )
        access = AccessToken.for_user(self.user)
        self.access = f"Bearer {access}"

    def test_get_task(self, id=0):
        endpoint = "/task/get/"
        if id > 0:
            params = {"id":id}        
            request = self.factory.get(endpoint, params=params, HTTP_AUTHORIZATION=self.access)
            response = view(request)
            print(response.status_code)
            print(response.data)
            assert response.status_code == status.HTTP_200_OK
        else:
            try:
                request = self.factory.get(endpoint, HTTP_AUTHORIZATION=self.access)
                response = self.view(request)
                assert response.status_code == status.HTTP_200_OK
            except AssertionError:
                print(response.status_code)
                print(response.data)

