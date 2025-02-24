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
    
