FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN pip install pip-tools && pip-compile --generate-hashes --output-file=requirements.txt requirements.in
RUN pip install -r requirements.txt

CMD ["pytest", "tests/api/test.py"]

