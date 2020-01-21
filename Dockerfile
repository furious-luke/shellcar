FROM python:3.8-alpine

RUN mkdir -p /app
COPY pyproject.toml /app
COPY poetry.lock /app
COPY setup.py /app
WORKDIR /app
RUN python setup.py install

COPY shellcar /app/shellcar
ENV FLASK_APP=/app/shellcar/main.py

CMD ["flask", "run", "-h", "0.0.0.0"]
