from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Libro

class BibliotecaTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)

    def test_crear_libro(self):
        data = {
            'titulo': 'Test Book',
            'autor': 'Test Author',
            'isbn': '1234567890123',
            'disponible': True,
            'fecha_publicacion': '2023-01-01'
        }
        response = self.client.post('/api/libros/', data, format='json')
        self.assertEqual(response.status_code, 201)