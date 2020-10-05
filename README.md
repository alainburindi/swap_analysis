# swap_analysis

[![Build Status](https://travis-ci.com/alainburindi/swap_analysis.svg?branch=develop)](https://travis-ci.com/alainburindi/swap_analysis)
[![codecov](https://codecov.io/gh/alainburindi/swap_analysis/branch/develop/graph/badge.svg?token=gLcYvCtswK)](https://codecov.io/gh/alainburindi/swap_analysis)

### Installing

```
    $ git clone https://github.com/alainburindi/swap_analysis.git
    $ cd swap_analysis
    $ python3 -m venv venv
    $ source venv/bin/activate
```

- Create .env and copy paste the environment variable from `.env_example` file that's already existent in the root directory

- Run the following commands

```
    $ pip install -r requirements.txt

```

- Create a postgreSQL database called `analysis` or any other name and provide the credentials(DB_NAME, DB_USER, DB_PASSWORD) in your `.env` file.

- Run the following commands to make the database migrations.

```
    $ python3 manage.py migrate
```

- Run the following commands to load the fixtures. these will create some data that can be used to test the app

```
    $ sh swap_analysis/fixtures/load_fixtures.sh
```

### Running the application

Run the command below to run the application locally.

```
  $ python3 manage.py runserver
```

### Running the tests

Run the command below to run the tests for the application.

```
    $ python manage.py test
```

### Installing using docker

check Docker installation that applies to you operating system. [Docker](https://docs.docker.com/get-docker/)

if you have docker installed run the following command in the root directory/folder.

```
    $ docker build .
    $ docker-compose build
```

### Running the application using Docker

```
    $ docker-compose up
```

If the app is not running. `exec` should be replaced by `run` in the following processes

### Loading the migrations

```
    $  docker-compose exec web sh -c "python manage.py migrate"
```

### Loading the fixtures

```
    $  docker-compose exec web sh -c "sh swap_analysis/fixtures/load_fixtures.sh"
```

Now you are good to go. Enjoy the functionalities

### Running the tests with Docker

```
    $ docker-compose exec web --rm sh -c "python manage.py test"
```

## Endpoints:

#### Authentication:

`POST /login`

```source-json
{
    "email": "attendant@ampersand.solar",
    "password": "Password"
}
```

#### Swap:

`GET /swaps`
Get all swaps list

`POST /swaps`

ceate a swap

```source-json
{
    "battery_out": "d734d9bc-573f-4c1e-8a02-adeae35dcbc1",
    "battery_in": "d734d9bc-573f-4c1e-8a02-adeae35dcbc1",
    "driver": "d734d9bc-573f-4c1e-8a02-adeae35dcbc1",
    "station": "d734d9bc-573f-4c1e-8a02-adeae35dcbc1",
    "driven_distance": 1.2,
    "out_state_of_charge": 60,
    "in_state_of_charge": 20,
    "used_energy": -3
}
```

For the endpoints bellow the date is optional. if it's not provided the today's date wille be considered

`GET /total_energy`
Get the total energy used per day

```source-json
{
    "date": "2020-10-10"
}
```

`GET /distance_driven`
Get the total drive distance per day

```source-json
{
    "date": "2020-10-10"
}
```

## To do:

Calculate the battery efficiency

### Deployment

Stagging link on heroku: [click here](https://fast-savannah-03659.herokuapp.com)
