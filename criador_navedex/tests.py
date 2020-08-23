import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from criador_navedex.models import Naver, Projeto
from criador_navedex.api.serializers import NaverSerializer, ProjetoSerializer


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            "username": "testcase1",
            "email": "email1@testcase.com",
            "password": "testcase"
        }

        response = self.client.post('/api/register/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
