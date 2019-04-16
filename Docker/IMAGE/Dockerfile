FROM python:2
MAINTAINER Samantha Comeau

ADD automate.py /
RUN pip install pyserial

ARG RW="read"
RUN if ["$RW"="read"]; then echo 'reading'; else echo 'writing'; fi 

CMD ["python", "automate.py", "-r", "-m", "98:D3:11:FC:1C:45"]

