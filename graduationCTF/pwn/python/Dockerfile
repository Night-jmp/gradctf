FROM ubuntu:latest
RUN apt update && apt install socat -y
RUN apt install python2 -y

RUN useradd --create-home --shell /bin/bash user

WORKDIR /home/user
COPY ./chal.py .
COPY ./flag.txt .
COPY ./password.txt .

EXPOSE 5000


ENTRYPOINT ["socat", "tcp-l:5000,reuseaddr,fork", "EXEC:\"./chal.py\",pty,stderr"]
