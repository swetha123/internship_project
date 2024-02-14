FROM python:3.8-slim-buster
WORKDIR /service
COPY requirements.txt .
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT [ "streamlit","run"]
CMD ['app.py']

