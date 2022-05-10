from fastapi.testclient import TestClient
from app.database.test_db_config import temp_db, SessionLocal
from main import app
from app.models import BookStatus


client = TestClient(app)


@temp_db
def test_create_book():

    bookshelve = client.post("/api/books/bookshelve", json={"number": 3})

    response = client.post(
        "/api/books/",
        json={
            "title": "Hashim book",
            "price": 35.4,
            "bookshelve_id": bookshelve.json()["id"],
        },
    )

    assert response.status_code == 200

    expected_response = {
        "id": 1,
        "status": BookStatus.PRESENT,
        "title": "Hashim book",
        "price": 35.4,
        "bookshelve_id": bookshelve.json()["id"],
    }

    assert response.json() == expected_response


@temp_db
def test_create_book_with_correct_status():

    bookshelve = client.post("/api/books/bookshelve", json={"number": 3})

    response_present = client.post(
        "/api/books/",
        json={
            "title": "Hashim book",
            "price": 35.4,
            "bookshelve_id": bookshelve.json()["id"],
        },
    )

    assert response_present.status_code == 200

    expected_response = {
        "id": 1,
        "status": BookStatus.PRESENT,
        "title": "Hashim book",
        "price": 35.4,
        "bookshelve_id": bookshelve.json()["id"],
    }

    assert response_present.json() == expected_response

    response_hold = client.post(
        "/api/books/",
        json={
            "title": "hold Hashim book",
            "price": 0,
        },
    )

    assert response_hold.status_code == 200

    expected_response = {
        "id": 2,
        "status": "HOLD",
        "title": "hold Hashim book",
        "price": 0.0,
        "bookshelve_id": None,
    }

    assert response_hold.json() == expected_response

    response_sold = client.post(
        "/api/books/",
        json={
            "title": "sold Hashim book",
            "price": 12,
        },
    )

    assert response_sold.status_code == 200

    expected_response = {
        "id": 3,
        "status": "SOLD",
        "title": "sold Hashim book",
        "price": 12,
        "bookshelve_id": None,
    }

    assert response_sold.json() == expected_response


@temp_db
def test_update_book():

    bookshelve = client.post("/api/books/bookshelve", json={"number": 3})

    create_response = client.post(
        "/api/books/",
        json={
            "title": "Hashim book",
            "price": 35.4,
            "bookshelve_id": bookshelve.json()["id"],
        },
    )

    assert create_response.status_code == 200

    update_response = client.patch(
        "/api/books/%s" % create_response.json()["id"],
        json={
            "title": "new Hashim book",
            "price": 44.4,
            "bookshelve_id": bookshelve.json()["id"],
        },
    )

    assert update_response.status_code == 200

    expected_response = {
        "id": create_response.json()["id"],
        "title": "new Hashim book",
        "status": "PRESENT",
        "price": 44.4,
        "bookshelve_id": bookshelve.json()["id"],
    }

    assert update_response.json() == expected_response

    hold_update_response = client.patch(
        "/api/books/%s" % create_response.json()["id"],
        json={"title": "new Hashim book", "price": 0, "bookshelve_id": 0},
    )

    assert hold_update_response.status_code == 200

    expected_response = {
        "id": create_response.json()["id"],
        "title": "new Hashim book",
        "status": "HOLD",
        "price": 0.0,
        "bookshelve_id": 0,
    }

    assert hold_update_response.json() == expected_response

    sold_update_response = client.patch(
        "/api/books/%s" % create_response.json()["id"],
        json={"title": "new Hashim book", "price": 10, "bookshelve_id": 0},
    )

    assert hold_update_response.status_code == 200

    expected_response = {
        "id": create_response.json()["id"],
        "title": "new Hashim book",
        "status": "SOLD",
        "price": 10,
        "bookshelve_id": 0,
    }

    assert sold_update_response.json() == expected_response


@temp_db
def test_create_bookshelve():

    response = client.post("/api/books/bookshelve", json={"number": 3})

    assert response.status_code == 200

    expected_response = {"id": 1, "number": 3}

    assert response.json() == expected_response


@temp_db
def test_delete_bookshelve():

    bookshelve = client.post("/api/books/bookshelve", json={"number": 3})

    book = client.post(
        "/api/books/",
        json={
            "title": "Hashim book",
            "price": 35.4,
            "bookshelve_id": bookshelve.json()["id"],
        },
    )

    no_price_book = client.post(
        "/api/books/",
        json={
            "title": "zero Hashim book to hold",
            "price": 0,
            "bookshelve_id": bookshelve.json()["id"],
        },
    )

    delete_bookshelve_response = client.delete(
        "/api/books/bookshelve/%s" % bookshelve.json()["id"]
    )

    assert delete_bookshelve_response.status_code == 204

    book_after_delete_bookshelve = client.get("/api/books/%s" % book.json()["id"])

    assert book_after_delete_bookshelve.json()["status"] == "SOLD"


@temp_db
def test_delete_book():

    book = client.post("/api/books/", json={"title": "Hashim book", "price": 35.4})

    response = client.delete("/api/books/%s" % book.json()["id"])

    assert response.status_code == 204
