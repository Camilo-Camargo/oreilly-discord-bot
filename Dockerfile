from alpine:3.18

COPY . /app
WORKDIR /app
RUN apk add python3
RUN python3 -m venv .oreilly-discord-bot
RUN source ./.oreilly-discord-bot/bin/activate &&\
	   pip install -r ./requirements.txt &&\
	   pip install -r ./third_party/safaribooks/requirements.txt
CMD .oreilly-discord-bot/bin/python3 ./main.py
