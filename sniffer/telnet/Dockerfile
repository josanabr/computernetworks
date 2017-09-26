FROM ubuntu
MAINTAINER John Sanabria - john.sanabria@gmail.com
RUN apt-get -y update
RUN apt-get -y install xinetd telnetd openssl
COPY telnet /etc/xinetd.d/telnet
RUN useradd -d /home/usuario -s /bin/bash -p $(openssl passwd -1 usuario) usuario
EXPOSE 23
ENTRYPOINT /etc/init.d/xinetd start && bash
