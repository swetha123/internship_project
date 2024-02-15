FROM python:3.8-slim-buster
CMD mkdir -p /app
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
ENTRYPOINT [ "streamlit","run"]
CMD ["app.py"]

