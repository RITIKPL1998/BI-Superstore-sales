#!/bin/bash

pip install --user -r /requirements.txt

airflow db init

airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

# Start the scheduler in the background
airflow scheduler &

# Start the webserver in foreground
exec airflow webserver
