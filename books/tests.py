# myapp/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from .models import Book
from django.contrib.auth.models import User

class BookApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/books/'
        
        # create unit testing user
        self.user = User.objects.create_user(username='test', password='101080')
        self.client.login(username='test', password='101080')

        # create book
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': timezone.now().date().isoformat()
        }
        self.book = Book.objects.create(**self.book_data)

    def test_get_books(self):
        response = self.client.get(self.url)
        print(response.data)  # debug
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)  # check 'results'
        results = response.data['results']
        self.assertTrue(isinstance(results, list))  # check 'results'
        if len(results) > 0:
            self.assertIn('title', results[0])
            self.assertEqual(results[0]['title'], self.book_data['title'])

    def test_get_book_by_id(self):
        response = self.client.get(f'{self.url}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_create_book(self):
        response = self.client.post(self.url, self.book_data, format='json')
        print(response.data)  # Añade esta línea para depuración
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_update_book(self):
        update_data = {
            'title': 'Updated Title',
            'author': 'Updated Author', 
            'published_date': self.book_data['published_date']
        }
        response = self.client.put(f'{self.url}{self.book.id}/', update_data, format='json')
        print(response.data)  # debug
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], update_data['title'])
        self.assertEqual(response.data['author'], update_data['author'])

    def test_delete_book(self):
        response = self.client.delete(f'{self.url}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # check last delete
        response = self.client.get(f'{self.url}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
