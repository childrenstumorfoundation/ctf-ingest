FROM openjdk:8-jre

LABEL maintainer='David Riordan <dr@daveriordan.com>'

WORKDIR sfdccommander

RUN wget -O sfdcCommander.zip \
  https://github.com/jwiesel/sfdcCommander/releases/download/v0.5/sfdcCommander-0.5-Portable.zip && \
  unzip sfdcCommander.zip && \
  rm sfdcCommander.zip
