FROM debian:latest
RUN rm /bin/bash
RUN useradd -m shhhhhh -s /bin/sh;
RUN echo "shhhhhh:U6aMy0wojraho" | chpasswd -e
RUN echo "vulncon{TW9kZS1TX0hleGNvZGUK}" > /root/flag.txt
RUN chmod 600 /root/flag.txt
RUN apt update
RUN apt install -y libcap2-bin
RUN apt install -y python2.7
RUN setcap cap_setuid+ep /usr/bin/python2.7
RUN chsh -s /bin/sh
CMD clear; su - shhhhhh
