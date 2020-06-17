FROM python:3.7-stretch

RUN apt-get -y update && apt-get -y upgrade && apt-get install nginx git -y cron

RUN git clone https://github.com/onsplatform/platform_reproduction.git /var/www/reproduction

WORKDIR /var/www/reproduction

RUN pip install pipenv gunicorn

RUN pipenv  install --system --deploy

RUN cp /var/www/reproduction/deploy/reproduction.nginx /etc/nginx/sites-available/reproduction

RUN mkdir /var/log/reproduction \
 && rm -rf /etc/nginx/sites-enabled/default \
 && ln -s /etc/nginx/sites-available/reproduction /etc/nginx/sites-enabled/reproduction

ENV GUNICORN_TIMEOUT 3000

EXPOSE 9098

RUN cp /var/www/reproduction/deploy/docker_entrypoint.sh /docker_entrypoint.sh
RUN cp /var/www/reproduction/deploy/reproduction.sh /reproduction.sh

RUN chmod +x /docker_entrypoint.sh
RUN chmod +x /reproduction.sh

ENTRYPOINT ["sh", "/docker_entrypoint.sh"]