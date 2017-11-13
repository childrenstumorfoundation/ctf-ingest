FROM jupyter/scipy-notebook

LABEL maintainer='David Riordan <dr@daveriordan.com>'

RUN conda install --quiet --yes \
  'psycopg2=2.7.3.*'

RUN pip install \
  pandasticsearch \
  elasticsearch \
  csv2es \
  plotly

USER root
RUN wget -O pgfutter https://github.com/lukasmartinelli/pgfutter/releases/download/v1.1/pgfutter_linux_amd64 && \
  chmod +x pgfutter && \
  mv pgfutter /usr/local/bin/pgfutter

RUN conda install --quiet --yes \
  csvkit

USER $NB_USER
