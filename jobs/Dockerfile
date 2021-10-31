FROM postgis/postgis
ARG POSTGRES_DBNAME
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD

#Create and cd into /code/ on the container, then copy all of the files in the same directory as this Dockerfile from the normal filesystem into /code/ on the container
WORKDIR /code
COPY . .

COPY crontab /etc/cron.d/cron-backups
RUN chmod 0644 /etc/cron.d/cron-backups
RUN touch /var/log/cron.log

RUN touch /root/.pgpass
RUN echo ceom_db:5432:${POSTGRES_DBNAME}:${POSTGRES_USER}:${POSTGRES_PASSWORD} > /root/.pgpass
RUN chmod 0600 /root/.pgpass

RUN apt-get update
RUN apt-get install -y python3 python3-pip rsync
RUN pip3 install requests

RUN apt-get -y install cron
RUN crontab /etc/cron.d/cron-backups
CMD cron && tail -f /var/log/cron.log

