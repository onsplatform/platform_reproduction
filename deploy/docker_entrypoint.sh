#!/usr/bin/env bash

service nginx start

gunicorn wsgi:reproduction_api --name ReproductionAPI --workers 3 --bind=unix:/var/www/reproduction/gunicorn.sock --log-level=debug --log-file=- --timeout $GUNICORN_TIMEOUT
