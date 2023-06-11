FROM alpine:3.18

COPY . /app
WORKDIR /app
RUN apk add python3
RUN python3 -m venv .oreilly-discord-bot
RUN source ./.oreilly-discord-bot/bin/activate &&\
	   pip install -r ./requirements.txt &&\
	   pip install -r ./third_party/safaribooks/requirements.txt

RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk add calibre@testing

ENV PATH="/usr/bin:${PATH}"

CMD .oreilly-discord-bot/bin/python3 ./main.py
