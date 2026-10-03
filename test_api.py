import requests

BASE_URL = "http://localhost:8000"


def test_get_books():
    response = requests.get(f"{BASE_URL}/books")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_book():
    book = {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "price": 29.99
    }

    response = requests.post(
        f"{BASE_URL}/books",
        json=book
    )

    assert response.status_code == 201
    assert response.json() == book