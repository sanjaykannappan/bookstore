import httpx
import pytest
import random

@pytest.mark.asyncio
async def test_app_health():
   
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:

        # Checking the health of application
        '''
            curl -X 'GET' \
                'http://127.0.0.1:8000/health' \
                -H 'accept: application/json'

            Response:- 
                statuscode == 200
            Respbody:-
                {
                    "status": "up"
                }
    
        '''
         
        
        response = await client.get("/health", headers={"accept": "application/json"})
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "up"

        # Signup New User
        '''
        curl -X 'POST' \
                'http://127.0.0.1:8000/signup' \
                -H 'accept: application/json' \
                -H 'Content-Type: application/json' \
                -d '{
                
                "email": "test@test.com",
                "password": "abcd123"
                }'

        Response:-
            statuscode = 200
        Respbody:-
            {
                "message": "User created successfully"
            }
        '''
        random_int = str(random.randint(1, 100000))
        email = "test"+random_int+"@test,com"
        passwd = "abcd123" + random_int
        response = await client.post("/signup", headers={"accept": "application/json", "Content-Type": "application/json"}, json={
            "email": email,
            "password": passwd
        })
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "User created successfully"

        #login to get JWT token

        '''
        curl -X 'POST' \
            'http://127.0.0.1:8000/login' \
            -H 'accept: application/json' \
            -H 'Content-Type: application/json' \
            -d '{
            "email": "test@test.com",
            "password": "abcd123"
            }'

        Response:-
            statuscode = 200
        Respbody:-
            {
                "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0QHRlc3QuY29tIiwiZXhwIjoxNzM5NzYzMzU2fQ.iX-TZqDFxvwKLDNFxFi24dIepfUWnZWPFy89GRYe1ac",
                "token_type": "bearer"
            }
        
        '''
        response = await client.post("/login", headers={"accept": "application/json", "Content-Type": "application/json"}, json={
            "email": email,
            "password": passwd
        })
        assert response.status_code == 200
        data = response.json()
        assert data["token_type"] == "bearer"
        access_token = data["access_token"]

        # Create Books record
        '''
        curl -X 'POST' \
            'http://127.0.0.1:8000/books/' \
            -H 'accept: application/json' \
            -H 'Content-Type: application/json' \
            -d '{
            "id": 1,
            "name": "test book",
            "author": "test book author",
            "published_year": 1989,
            "book_summary": "test summary"
            }
        
        '''

        response = await client.post("/books/", headers={"accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer "+access_token}, json={
            "id": int(random_int),
            "name": "test book",
            "author": "test book author",
            "published_year": 1989,
            "book_summary": "test summary"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == int(random_int)
        assert data["name"] == "test book"
        assert data["author"] == "test book author"
        assert data["published_year"] == 1989
        assert data["book_summary"] == "test summary"

        #Get Created Book

        '''
        curl -X 'GET' \
            'http://127.0.0.1:8000/books/57938' \
            -H 'accept: application/json' \
            -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0QHRlc3QuY29tIiwiZXhwIjoxNzM5NzY0MDY2fQ.O6Ak_osIGgNnqvpK8WW8grep9xnm4hOpgxdjey0BvxU'

        Response:-
            statuscode = 200
        Respbody
            {
                "published_year": 1989,
                "name": "test book",
                "book_summary": "test summary",
                "author": "test book author",
                "id": 57938
            }
        '''

        response = await client.get("/books/"+random_int, headers={"accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer "+access_token})
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == int(random_int)
        assert data["name"] == "test book"
        assert data["author"] == "test book author"
        assert data["published_year"] == 1989
        assert data["book_summary"] == "test summary"

        # Update Book record

        '''
        curl -X 'PUT' \
            'http://127.0.0.1:8000/books/57938' \
            -H 'accept: application/json' \
            -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0QHRlc3QuY29tIiwiZXhwIjoxNzM5NzY0MDY2fQ.O6Ak_osIGgNnqvpK8WW8grep9xnm4hOpgxdjey0BvxU' \
            -H 'Content-Type: application/json' \
            -d '{
                "published_year": 1989,
                "name": "test book",
                "book_summary": "test summary",
                "author": "test book author",
                "id": 57938
            }'

        Response:-
            statuscode = 200
        Respbody:-
            {
                "published_year": 1989,
                "name": "test book",
                "book_summary": "test summary",
                "author": "test book author",
                "id": 57938
            }

        '''
        response = await client.put("/books/"+random_int, headers={"accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer "+access_token}, json={
            "id": int(random_int),
            "name": "test book",
            "author": "test book author",
            "published_year": 1990,
            "book_summary": "test summary new"
        })

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == int(random_int)
        assert data["name"] == "test book"
        assert data["author"] == "test book author"
        assert data["published_year"] == 1990
        assert data["book_summary"] == "test summary new"

        # Get Updated Book

        response = await client.get("/books/"+random_int, headers={"accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer "+access_token})
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == int(random_int)
        assert data["name"] == "test book"
        assert data["author"] == "test book author"
        assert data["published_year"] == 1990
        assert data["book_summary"] == "test summary new"

        # Get Books as list
        '''
        curl -X 'GET' \
            'http://127.0.0.1:8000/books/' \
            -H 'accept: application/json' \
            -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0QHRlc3QuY29tIiwiZXhwIjoxNzM5NzY0MDY2fQ.O6Ak_osIGgNnqvpK8WW8grep9xnm4hOpgxdjey0BvxU'

        Response:-
            statuscode = 200
        Respbody:-
           [
            {
                "published_year": 1989,
                "name": "test book",
                "book_summary": "test summary",
                "author": "test book author",
                "id": 20
            },
            {
                "published_year": 1989,
                "name": "test book",
                "book_summary": "test summary",
                "author": "test book author",
                "id": 57938
            }
        ] 
        '''
        response = await client.get("/books/", headers={"accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer "+access_token})
        assert response.status_code == 200
        datas = response.json()
        match = False
        for data in datas:
            if data["id"] == int(random_int):
                match = True
                assert data["id"] == int(random_int)
                assert data["name"] == "test book"
                assert data["author"] == "test book author"
                assert data["published_year"] == 1990
                assert data["book_summary"] == "test summary new"
        if not match :
            pytest.fail("Updated record not found from Get List")

        # Delete Book record
        '''
        curl -X 'DELETE' \
            'http://127.0.0.1:8000/books/20' \
            -H 'accept: application/json' \
            -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0QHRlc3QuY29tIiwiZXhwIjoxNzM5NzYzMzU2fQ.iX-TZqDFxvwKLDNFxFi24dIepfUWnZWPFy89GRYe1a'

        Response:-
            statuscode = 200

        Responsebody:-
            {
                "message": "Book deleted successfully"
            }

        '''

        response = await client.delete("/books/"+random_int, headers={"accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer "+access_token})

        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Book deleted successfully"


    
        
