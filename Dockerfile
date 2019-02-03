FROM python:3.7-alpine AS base

COPY . /a

RUN pip install flask flask-jsonpify flask-sqlalchemy flask-restful

RUN 

CMD python /a/sth.py

kaesjfhauyliaewfjihehiuf
