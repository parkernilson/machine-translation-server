FROM python:3.8-slim-buster

WORKDIR /code

# install tensorflow because it is large and we want to cache it. This way, we can change dependencies and rebuild faster.
RUN pip install tensorflow==2.3.1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "server.py" ]
