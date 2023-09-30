#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm meet_brief.wsgi:application --bind "0.0.0.0:${APP_PORT}"