FROM python:3.8-slim-buster
WORKDIR /service
COPY requirements.txt .
RUN pip install -r rewuirements.txt
ENTRYPOINT [ "python3", "app.py"]