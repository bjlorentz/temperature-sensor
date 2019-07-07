#!/bin/sh

uwsgi --http 0.0.0.0:8000 --wsgi-file server.py --callable app_dispatch