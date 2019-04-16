FROM python:2
MAINTAINER Samantha Comeau

ADD automate.py /
RUN pip install pyserial

ENV RW needed
ENV BIND false

ENV MAC needed
ENV MESSAGE needed
ENV PORT 0

RUN echo $RW

CMD ["sh", "-c", "python automate.py $BIND $RW $MAC $PORT $MESSAGE"]

