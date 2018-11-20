#!/bin/bash

function install_db_server {
    echo "Installing DB server"
    apt -y install postgresql
}

function install_memcached {
    echo "Installing memcached server"
    apt -y install memcached
}

function install_node {
    echo "Installing node server requirements"
    apt install -y libmemcached-dev python3-pip cifs-utils zlib1g-dev python3-dev build-essential
    pip3 install pylibmc psutil psycopg2-binary pyyaml requests
}

function install_core {
    echo "Installing core server requirements"
    pip3 install cherrypy jinja2 htmlmin
}


do_install_db=0
do_install_mc=0
do_install_node=0
do_install_core=0

read -p "Install DB server? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    do_install_db=1
fi

read -p "Install memcached server? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    do_install_mc=1
fi

read -p "Install node? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    do_install_node=1

    read -p "Install core server requirements? " -n 1 -r
    echo    # (optional) move to a new line
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        do_install_core=1
    fi
fi




echo ""

if [ $do_install_db == 1 ]; then
    install_db_server || exit 1
fi

if [ $do_install_mc == 1 ]; then
    install_memcached || exit 1
fi

if [ $do_install_node == 1 ]; then
    install_node || exit 1
fi

if [ $do_install_core == 1 ]; then
    install_core || exit 1
fi

