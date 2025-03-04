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






# Steps to run Unit tests

    1. pip install -r requirements.txt

    2. run the below command :

        pytest --cov=..\bookstore unitests 

        If HTML report need run below
        
        pytest --cov=..\bookstore unitests --cov-report=html


# Implementation Logic.

Database Test:
    1. In this test we have created the model values and assertion for the models which are defined in the database.py file

Bookmgmt Test:

    1.  Here we defined the mockdb as all the book releated create, get, update and delete needs database operation.

    2. We mocked the jwt token as all the methods in bookmgmt requires authentication "dependencies=[Depends(JWTBearer())"

    3. We started writing unittest for each method from bookmgmt
        - create_book
        - get_all_books
        - get_book_by_id
        - update_book
        - delete_book

    4. We tried to invoke all the functions of bookmgmt.py from our unnitest and wherever DB operations are expected we used the mockdb for create update, get and delete.

    5. Assert compaison is done with actual and expected values. 





# Please find CI-CD 

name: FastAPI CI Workflow

on:
  push:
    branches:
      - main  # Trigger workflow on pushes to the main branch
  pull_request:
    branches:
      - main  # Trigger workflow on pull requests targeting the main branch

jobs:
  build:
    runs-on: ubuntu-latest  # Use an Ubuntu runner

    steps:
        # Step 1: Checkout the repository
        - name: Checkout repository
        uses: actions/checkout@v2

        # Step 2: Set up Python 3.x
        - name: Set up Python 3.9
        uses: actions/setup-python@v2
        with:
            python-version: '3.13'  # You can adjust the version to match your environment

        # Step 3: Install dependencies
        - name: Install dependencies
        run: |
            pip install -r requirements.txt

        # Step 4: Run tests with unitest
        - name: Run tests
        run: |
            pip install -r unitests/requirements.txt
            pytest --cov=..\bookstore unitests   # Run tests, show output if they fail

        # step 5: Run Applicaton to check
        - name: Run application
        run : |
            uvicorn main:app

        # Step 6: Run  integration test
        - name: Run integration test
        run : |
            pytest ..\integration\bookstore_int_test.py  
    
