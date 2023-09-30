FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt

RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]

