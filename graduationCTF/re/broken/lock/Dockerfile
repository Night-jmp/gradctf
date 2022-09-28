FROM ubuntu:latest
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y libc6:i386
RUN apt-get install -y ucspi-tcp
RUN adduser noob
COPY * /
WORKDIR /
EXPOSE 1337
USER noob
CMD tcpserver -t 50 -RHl0 0.0.0.0 1337 ./airlock
