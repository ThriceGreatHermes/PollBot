FROM frolvlad/alpine-python3

ARG slack_token
ENV SLACK_TOKEN $slack_token

RUN mkdir /poll_bot
RUN cd poll_bot
ADD requirements.txt ./requirements.txt
ADD ./poll_bot/ ./poll_bot/
RUN pip3 install -r requirements.txt

ENTRYPOINT python3 ./poll_bot/run_bot.py --token $SLACK_TOKEN