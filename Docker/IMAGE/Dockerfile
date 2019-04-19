FROM python:2
MAINTAINER Samantha Comeau

ADD automate.py /

RUN pip install pyserial

ENV RW needed

ENV MESSAGE needed
ENV PORT needed

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
USER docker


CMD ["sh", "-c", "python automate.py $RW $PORT $MESSAGE"]

