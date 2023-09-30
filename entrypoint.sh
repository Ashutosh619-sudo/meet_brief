#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm meet_brief.wsgi:application --bind "0.0.0.0:${APP_PORT}"

dop_v1_1f8fe730126c2819413e640a26675c126f6e55f0d353ec1b6259f9b704ed3408