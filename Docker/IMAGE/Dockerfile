FROM python:2
MAINTAINER Samantha Comeau

ADD automate.py /
ADD setup_port.sh /
ADD rfcomm /
ADD chmod /

RUN pip install pyserial

ENV RW needed
ENV BIND false

ENV MAC needed
ENV MESSAGE needed
ENV PORT 0

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
USER docker


CMD ["sh", "-c", "rfcomm release $PORT ; python automate.py $BIND $RW $MAC $PORT $MESSAGE"]

