# Steps to run Unit tests

    1. pip install -r requirements.txt

    2. run the below command :

        cd bookstore

        pytest --cov=..\bookstore unitests 

        If HTML report need run below
        
        pytest --cov=..\bookstore unitests --cov-report=html

