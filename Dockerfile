FROM python:3.9.7-slim

WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install --upgrade pip

COPY requirements.txt .

RUN apt-get update \
  && apt-get -y install libpq-dev gcc

RUN /opt/venv/bin/pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]