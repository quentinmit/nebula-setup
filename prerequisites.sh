#!/bin/bash

apt -y install \
    python \
    python-psycopg2 \
    python-pylibmc \
    python-psutil \
    python-cairo \
    python-imaging \
    python-gtk2

pip install cherrypy
