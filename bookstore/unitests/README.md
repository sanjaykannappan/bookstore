# Steps to run Unit tests

    1. pip install -r requirements.txt

    2. run the below command :

        cd bookstore

        pytest --cov=..\bookstore unitests 

        If HTML report need run below
        
        pytest --cov=..\bookstore unitests --cov-report=html


## Unit test coverage report from my local setup

            Name                        Stmts   Miss  Cover
        -----------------------------------------------
        bookmgmt.py                    42      3    93%
        constants.py                    3      0   100%
        database.py                    27      4    85%
        main.py                        33     16    52%
        middleware.py                  22      4    82%
        unitests\__init__.py            0      0   100%
        unitests\bookmgmt_test.py     100      5    95%
        unitests\database_test.py      19      0   100%
        utils.py                       11      1    91%
        -----------------------------------------------
        TOTAL                         257     33    87%

