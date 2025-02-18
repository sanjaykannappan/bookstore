import httpx
import pytest

'''
reference from swagger
Request
    curl -X 'POST' \
    'http://127.0.0.1:8000/signup' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "id": 1,
    "email": "test@testing.com",
    "password": "123abc"
    }'


Response 

    statuscode=200

    {
    "message": "User created successfully"
    }

'''

@pytest.mark.asyncio
async def test_create_user():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8000/signup", json={"id":
        6, "email": "test6@testing.com", "password":
        "123456abc"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User created successfully"



'''
reference from swagger
Request
    curl -X 'POST' \
    'http://127.0.0.1:8000/login' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "id": 1,
    "email": "test@testing.com",
    "password": "123abc"
    }'


Response 

    statuscode=200

{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0QHRlc3RpbmcuY29tIiwiZXhwIjoxNzM5Njg4NjIzfQ.BEOaBMohvtQQGU_rP9uMrc1n5pR5s5yCGS2CCx9rvxc",
  "token_type": "bearer"
}

'''


@pytest.mark.asyncio
async def test_login():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8000/login", json={"id":
        6, "email": "test6@testing.com", "password":
        "123456abc"})
    assert response.status_code == 200
    data = response.json()
    assert data["token_type"] == "bearer"


'''
reference from swagger
Request

    curl -X 'GET' \
    'http://127.0.0.1:8000/health' \
    -H 'accept: application/json'
    }'


Response 

    statuscode=200

    {
    "status": "up"
    }

'''


@pytest.mark.asyncio
async def test_health():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "up"


