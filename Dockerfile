FROM python:3.10

WORKDIR /project

COPY ./project/ /project/

RUN pip install poetry
RUN poetry install

CMD poetry run python main.py
# CMD poetry run uvicorn app.api:app --host 0.0.0.0 --port 80