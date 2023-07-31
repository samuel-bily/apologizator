FROM docker.io/python:3.7


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV GUNICORN_CMD_ARGS="-b=0.0.0.0:5000"
COPY . .

EXPOSE 5000

CMD [ "gunicorn", "main:app" ]
