FROM python:3.7-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && \
    useradd -m chad && \
    chown -R chad .

USER chad

EXPOSE 5000
CMD ["python", "main.py"] 
