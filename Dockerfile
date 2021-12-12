FROM debian:buster

MAINTAINER Ahmad Ali Moshtaghi

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get install -y \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	git \
	libmariadbclient-dev \ 
	cron && \
        rm -rf /var/lib/apt/lists/* && \
	pip3 install uwsgi && \
	mkdir -p /var/www

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

COPY requirements.txt /var/www
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /var/www/requirements.txt

# add (the rest of) our code
COPY . /var/www

WORKDIR /var/www

RUN chmod +x entrypoint.sh

EXPOSE 80

#RUN cd /var/www/ && python3 manage.py collectstatics
ENTRYPOINT ["/var/www/entrypoint.sh"]
