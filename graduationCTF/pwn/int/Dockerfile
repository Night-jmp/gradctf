FROM ubuntu:latest
RUN apt update && apt install socat -y

RUN useradd --create-home --shell /bin/bash user

WORKDIR /home/user
COPY ./chal .
COPY ./flag.txt .

EXPOSE 5000


ENTRYPOINT ["socat", "tcp-l:5000,reuseaddr,fork", "EXEC:\"./chal\",pty,stderr"]
