#!/bin/sh
sudo apt-get -y update
LIST_OF_APPS="aptitude build-essential tree curl git htop libffi-dev libssl-dev libxml2 libxml2-dev libxslt1-dev python python-dev python-pip python-software-properties python-virtualenv tig tmux uwsgi vim wget zlib1g-dev libmysqlclient-dev uwsgi-plugin-python3 libjpeg-dev libncurses5-dev libmagickwand-dev libffi-dev libav-tools libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev"

sudo apt-get install -y $LIST_OF_APPS
sudo apt-get -y update

# For personal use
echo "alias deploy='cp /srv/main.py myapp/. && cp /srv/*.kv myapp/. && buildozer android debug && mv bin/*.apk /srv/.'" >> .bashrc
