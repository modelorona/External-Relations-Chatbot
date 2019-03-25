# How to set up the Django server

The server has to be on the same server as the client.

Use Python 3.6 or above.

As currently all sensitive information is hard-coded, there is no extra setup needed for environmental variables.

Check the wiki for admin user details.

## Setup
Make sure to 
```bash
$ pip install -r requirements.txt
```

or if you are not using a virtual environment,
```bash
$ pip3 install -r requirements.txt
```

when in the folder with that file. It is recommended to run the server in a virtual environment.

## Running the server
To run the server itself, in the folder where ```manage.py``` exists, run
```bash
$ python manage.py runserver 5000
```

or if you are not using a virtual environment,
```bash
$ python3 manage.py runserver 5000
```

It is important to run it on port 5000 because to send an email, the client makes a post request to that url.

## How to test
Within the folder that contains ```manage.py```, run

```bash
$ python manage.py test
```

or if you are not using a virtual environment,
```bash
$ python3 manage.py test
```

