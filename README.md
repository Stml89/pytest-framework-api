## About

---
This is a simple example of a test automation project for testing [Booker broker](https://restful-booker.herokuapp.com/apidoc/), using [Pytest](https://docs.pytest.org/en/stable/),
and [allure](https://allurereport.org/docs/) for reporting.
Repository have a general structure to help you organize and create frameworks from scratch.

Made by Siarhei Stamal for Python Test Automation course.

## Project structure

---
```
/pytest-framework
├── .github
│   ├── workflows
│   │   ├── flake8.yaml
│   │   ├── ...
├── tests
│   ├── conftest.py
│   ├── test_booking.py
├── utils
│   ├── api
│   │   ├── auth.py
│   │   ├── booking.py
│   ├── clients
│   │   ├── http
│   │   │   ├── builder.py
│   │   │   ├── client.py
│   ├── models
│   │   ├── auth.py
│   │   ├── booking.py
│   ├── validate
│   │   ├── schema.py
│   ├── assertions.py
│   ├── random_generator.py
│   ├── routes.py
├── allure-results
│   ├── *.json
│   ├── *.txt
├── .gitignore
├── pyproject.toml
├── .env
├── settings.py
├── pytest.ini
├── README.md
├── requirements.txt
└── LICENSE
```

## Usage

---
### How to install

1. Clone this repository
```bash
    $ git clone <URL>
```
2. Create virtual environment, activate it:
```bash
    $ pip install virtualenv
    $ cd ~/projects/pytest-framework
    $ virtualenv venv
    $ source venv/bin/activate
```
3. Install dependencies
```bash
    $ pip install -r requirements.txt
```
### How to run tests
1. To execute ALL tests w/ DEBUG log level
```bash
    $ pytest . --log-level=DEBUG
```
2. To execute ALL API test suite
```bash
    $ pytest . -m login
```

### How to [build report](https://allurereport.org/docs/how-it-works/)
```bash
    $ allure serve
    or
    allure generate
```

### Available markers:
 + `api - to execute all API test cases`
 + `bookings - to execute test cases related to BOOKING functionality`
