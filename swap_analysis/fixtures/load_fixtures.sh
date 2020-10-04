#!/bin/bash

# the scrip to load data into the database
# should be arranged according to dependency of models

python3 manage.py loaddata swap_analysis/fixtures/authentication.json &&
python3 manage.py loaddata swap_analysis/fixtures/station.json &&
python3 manage.py loaddata swap_analysis/fixtures/attendant.json &&
python3 manage.py loaddata swap_analysis/fixtures/driver.json &&
python3 manage.py loaddata swap_analysis/fixtures/motor.json &&
python3 manage.py loaddata swap_analysis/fixtures/battery.json &&
python3 manage.py loaddata swap_analysis/fixtures/station.json &&
python3 manage.py loaddata swap_analysis/fixtures/swap.json
