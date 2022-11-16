FROM python:3.8
EXPOSE 8080

WORKDIR /app

COPY . /app/
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "./entrypoint.sh"]

ENTRYPOINT python main.py
