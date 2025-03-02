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

