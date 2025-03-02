# Integration Test Steps

### clone the code:-

    git clone 

### Pytest Steps:-

    cd integrationtest

    pytest bookstore_int_test.py


# Implementation logic:-

Step 1 : 
    Setup a async client which points to the running bookstore application 
        async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:

Step 2: 
    Identify all the right apis and plan the flow
        1. Health check
        2. Signup
        3. Login and get the token in a vairable
        4. Create the book 
        5. Get the book
        6. Update the book 
        7. Get book and books
        8. Delete the created book
    
    -  We have only signup option and we designed this test to run the flow again and again. When we use the same signup data, it will fail, so we have generated a random id which we attach to the mail and password so that in every run a unique signup user will happen and it will follow the step from 3 to 8 as mentioned above

- Here we have implemented only the positive scenario in the assert equal comparision. We ran the book store app and accessed the swagger http://127.0.0.1:8000/docs , using swagger have tried the positive scenarios, same is moved under this test.