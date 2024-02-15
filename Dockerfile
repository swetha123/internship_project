FROM python:3.8-slim-buster
cmd mkdir -p /app
WORKDIR /app
copy requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8501
ENTRYPOINT [ "streamlit","run"]
CMD ["app.py"]

