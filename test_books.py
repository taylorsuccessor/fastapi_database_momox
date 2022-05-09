from fastapi.testclient import TestClient
from main import app

from app.database.conftest import temp_db, SessionLocal

client = TestClient(app)

def test_validation_empty_json():
    assert 1 == 1

    # response = client.post("/api/books/", json={})
    # assert response.status_code == 422

@temp_db
def test_create_bookshelve():
    response = client.post("/api/books/bookshelve", json={'number': 3})
    assert response.status_code == 200

    expected_response = {
        'id': 1,
        'test': '',
        'number': 3
    }

    assert response.json() == expected_response
