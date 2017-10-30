FROM jwater7/mpv
LABEL maintainer "j"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 python-setuptools python-pip curl \
        supervisor \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

RUN pip install schedule

EXPOSE 9001

COPY supervisor_conf/supervisord-nodaemon.conf /etc/supervisor/conf.d/
COPY supervisor_conf/supervisord-http-server.conf /etc/supervisor/conf.d/
COPY supervisor_conf/scheduler.conf /etc/supervisor/conf.d/

COPY scheduler/* /usr/share/scheduler/

COPY job.conf /data/
RUN ln -s /data/job.conf /etc/supervisor/conf.d/job.conf
COPY jobschedule.py /data/

VOLUME /data

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

