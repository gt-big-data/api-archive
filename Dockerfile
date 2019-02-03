FROM python:3.7-alpine AS base

COPY . /a

RUN

CMD python /a/sth.py

