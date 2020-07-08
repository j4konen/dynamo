FROM python:3.6-alpine

RUN adduser -D dynamo
WORKDIR /home/dynamo

RUN python -m venv venv
RUN venv/bin/pip install flask
RUN venv/bin/pip install requests
RUN venv/bin/pip install gunicorn

COPY app ./
COPY boot.sh ./
RUN chmod +x boot.sh

RUN chown -R dynamo:dynamo ./
USER dynamo

EXPOSE 8003
ENTRYPOINT ["./boot.sh"]