from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.fixture
def create_book(api_client):
    def do_create_book(data):
        response = api_client.post('/api/book/book/', data)
        return response
    return do_create_book


@pytest.mark.django_db
class TestCreateBook:
    def test_create_book_returns_201(self, create_book):
        response = create_book({
            'title': 'Django'
        })

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] is not None
        assert response.data['id'] is not None

    def test_create_book_payload_if_invalid_returns_400(self, create_book):
        response = create_book({
            'title': ''
        })

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
