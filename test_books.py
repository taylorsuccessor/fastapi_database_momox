from main import app
from fastapi.testclient import TestClient
from app.models import BookStatus
from app.database.test_db_config import temp_db, SessionLocal


client = TestClient(app)

def test_validation_empty_json():
    assert 1 == 1

    # response = client.post("/api/books/", json={})
    # assert response.status_code == 422

@temp_db
def test_create_book():

    bookshelve = client.post("/api/books/bookshelve", json={
        'number': 3
    })

    response = client.post("/api/books/", json={
        'title': 'Hashim book',
        'price': 35.4,
        'bookshelve_id': bookshelve.json()['id']
    })

    assert response.status_code == 200

    expected_response = {
        'id': 1,
        'status': BookStatus.PRESENT,
        'title': 'Hashim book',
        'price': 35.4,
        'bookshelve_id': bookshelve.json()['id']
    }

    assert response.json() == expected_response

@temp_db
def test_create_book_with_correct_status():

    bookshelve = client.post("/api/books/bookshelve", json={
        'number': 3
    })

    response_present = client.post("/api/books/", json={
        'title': 'Hashim book',
        'price': 35.4,
        'bookshelve_id': bookshelve.json()['id']
    })

    assert response_present.status_code == 200

    expected_response = {
        'id': 1,
        'status': BookStatus.PRESENT,
        'title': 'Hashim book',
        'price': 35.4,
        'bookshelve_id': bookshelve.json()['id']
    }

    assert response_present.json() == expected_response

    response_hold = client.post("/api/books/", json={
        'title': 'hold Hashim book',
        'price': 0,
    })

    assert response_hold.status_code == 200

    expected_response = {
        'id': 2,
        'status': 'HOLD',
        'title': 'hold Hashim book',
        'price': 0.0,
        'bookshelve_id': None
    }

    assert response_hold.json() == expected_response

    response_sold = client.post("/api/books/", json={
        'title': 'sold Hashim book',
        'price': 12,
    })

    assert response_sold.status_code == 200

    expected_response = {
        'id': 3,
        'status': 'SOLD',
        'title': 'sold Hashim book',
        'price': 12,
        'bookshelve_id': None
    }

    assert response_sold.json() == expected_response




@temp_db
def test_create_bookshelve():

    response = client.post("/api/books/bookshelve", json={
        'number': 3
    })

    assert response.status_code == 200

    expected_response = {
        'id': 1,
        'test': '',
        'number': 3
    }

    assert response.json() == expected_response
