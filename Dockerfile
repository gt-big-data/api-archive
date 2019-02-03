FROM python:3.7-alpine AS base

COPY /a .

RUN pip install flask flask-jsonpify flask-sqlalchemy flask-restful gunicorn

EXPOSE 9001

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:9001", "sth:hello_world"]

#CMD python /a/sth.py


#kaesjfhauyliaewfjihehiuf
