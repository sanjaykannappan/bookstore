from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import pytest

from main import app
from middleware import JWTBearer # Import your JWTBearer dependency
from sqlalchemy.orm import Session
from database import get_db, Book
from bookmgmt import create_book
from utils import create_access_token
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


# Mocking the database session
@pytest.fixture
def mock_db():
    mock_db_session = MagicMock(spec=Session)
    yield mock_db_session


# Mocking the JWTBearer dependency to always return a valid token
@pytest.fixture
def mock_jwt():
    # Here, we'll just mock the JWTBearer to return a valid token for any request
    app.dependency_overrides[JWTBearer] = lambda: True  # Always authenticate successfully


# Create a test client to send requests to the FastAPI app
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


# Test for the POST /books/ endpoint
def test_create_book(client, mock_db, mock_jwt):
    # Create a fake book object to send in the request
    token = create_access_token(data={"sub": "testuser"})
    new_book_data = {
        "id": 1,
        "name": "Test",
        "author": "Test Author",
        "published_year": 2010,
        "book_summary": "test summary"
    }

    # Mock the database session behavior
    mock_db.add.return_value = None  # Simulate add behavior
    mock_db.commit.return_value = None  # Simulate commit behavior
    mock_db.refresh.return_value = None  # Simulate refresh behavior

    # Override the FastAPI dependency to use our mocked database session
    app.dependency_overrides[get_db] = lambda: mock_db

    # Send a POST request to the /books/ endpoint
    response = client.post("/books/", json=new_book_data,headers={"Authorization": f"Bearer {token}"})
    print("response::::", response)

    # Assertions
    assert response.status_code == 200  
    assert response.json()["id"] == new_book_data["id"]  
    assert response.json()["name"] == new_book_data["name"]  
    assert response.json()["author"] == new_book_data["author"]  
    assert response.json()["published_year"] == new_book_data["published_year"]
    assert response.json()["book_summary"] == new_book_data["book_summary"]

    # Ensure the db.add, db.commit, and db.refresh methods were called on the mock_db
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

    


# Test for the Get /books/ endpoint
def test_get_books(client, mock_db, mock_jwt):
    # Create a fake book object to send in the request
    token = create_access_token(data={"sub": "testuser"})
    app.dependency_overrides[get_db] = lambda: mock_db

    # Send a POST request to the /books/ endpoint
    response = client.get("/books/", headers={"Authorization": f"Bearer {token}"})
    #print("response::::", response)

    # Assertions
    assert response.status_code == 200  # Assert that the response status code is 200

    for resp in response.json():
        assert resp.json()["id"] == 1
        assert resp.json()["name"] == "Test"
        assert resp.json()["author"] == "Test Author"
        assert resp.json()["published_year"] == 2010
        assert resp.json()["book_summary"] == "test summary"

# Test for the Get /books/{book_id} endpoint
def test_get_book(client, mock_db, mock_jwt):
    # Create a fake book object to send in the request
    token = create_access_token(data={"sub": "testuser"})
    app.dependency_overrides[get_db] = lambda: mock_db

    mock_book = MagicMock()
    mock_book.id = 1
    mock_book.name = "Test"
    mock_book.author = "Test Author"
    mock_book.published_year = 2010
    mock_book.book_summary = "test summary"

    # Mock the database session and its query method
   
    mock_db.query().filter().first.return_value = mock_book
   
    # Send a POST request to the /books/ endpoint
    response = client.get("/books/1", headers={"Authorization": f"Bearer {token}"})
    #print("response::::", response)

    # Assertions
    assert response.status_code == 200  # Assert that the response status code is 200
    assert response.json()['id'] == 1
    assert response.json()['name'] == "Test"
    assert response.json()['author'] == "Test Author"
    assert response.json()['published_year'] == 2010
    assert response.json()["book_summary"] == "test summary"

# Test for the Update /books/{book_id} endpoint
def test_update_book(client, mock_db, mock_jwt):
    # Create a fake book object to send in the request
    token = create_access_token(data={"sub": "testuser"})
    app.dependency_overrides[get_db] = lambda: mock_db

    mock_book = MagicMock()
    mock_book.id = 1
    mock_book.name = "Test1"
    mock_book.author = "Test Author"
    mock_book.published_year = 1988
    mock_book.book_summary = "test summary"

    # Mock the database session and its query method
    mock_db.query().filter().first.return_value = mock_book
    
    new_book_data = {
        "id": 1,
        "name": "Test1",
        "author": "Test Author",
        "published_year": 2010,
        "book_summary": "test summary"
    }
    # Send a PUT request to the /books/ endpoint
    response = client.put("/books/1", json=new_book_data, headers={"Authorization": f"Bearer {token}"})
    #print("response::::", response)

    # Assertions
    assert response.status_code == 200  # Assert that the response status code is 200
    assert response.json()['id'] == 1
    assert response.json()['name'] == "Test1"
    assert response.json()['author'] == "Test Author"
    assert response.json()['published_year'] == 2010
    assert response.json()["book_summary"] == "test summary"

# Test for the delete /books/{book_id} endpoint
def test_delete_book(client, mock_db, mock_jwt):
    # Create a fake book object to send in the request
    token = create_access_token(data={"sub": "testuser"})
    app.dependency_overrides[get_db] = lambda: mock_db

    mock_book = MagicMock()
    mock_book.id = 1
    mock_book.name = "Test1"
    mock_book.author = "Test Author"
    mock_book.published_year = 1988
    mock_book.book_summary = "test summary"

    # Mock the database session and its query method
    mock_db.query().filter().first.return_value = mock_book
    mock_db.delete.return_value=None
    
   
    # Send a Delete request to the /books/ endpoint
    response = client.delete("/books/1", headers={"Authorization": f"Bearer {token}"})
    #print("response::::", response)

    # Assertions
    assert response.status_code == 200  # Assert that the response status code is 200
    assert response.json()['message'] == "Book deleted successfully"
   
    mock_db.delete.assert_called_once()