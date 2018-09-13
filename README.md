Nebula setup
============

Nebula database configuration tool

Prerequisites
-------------

Use prerequisites.sh script to install all required libraries and software

## Nginx

Nebula also needs nginx server with http push module to be installed.
Use [install.nginx.sh](https://github.com/immstudios/installers/blob/master/install.ffmpeg.sh)
and create /var/www/yoursitename/http.conf file.

Assuming your site name is "nebula" and nginx server is running on the same
machine as nebua itself, you may use following configuration:

```nginx
server {
    server_name             _;
    set $nxcore_root 		/mnt/nebula_01/.nx;

	add_header          Access-Control-Allow-Headers    'origin, content-type, accept, user-agent, referer' always;
	add_header          Access-Control-Allow-Origin     '*' always;

    location /export {
        root $nxcore_root;
    }

    location ~ /ws/(.*) {
        push_stream_subscriber websocket;
        push_stream_channels_path                   $1;
        push_stream_ping_message_interval           10s;
    }

    location /proxy/ {
        root $nxcore_root;
        mp4;
        mp4_max_buffer_size 5m;
    }

    location /thumb/ {
        root $nxcore_root;
    }

    location /api {
        proxy_pass          http://localhost:8080;
        proxy_set_header    Host $host;
        proxy_set_header    X-Real-IP $remote_addr;
    }

    location / {
        proxy_pass          http://localhost:8080;
        proxy_set_header    Host $host;
        proxy_set_header    X-Real-IP $remote_addr;
    }
}
```

## FFMpeg

Conversion nodes depend on ffmpeg. You may use
[this script](https://github.com/immstudios/installers/blob/master/install.ffmpeg.sh)
to install it.


Site template
-------------

Create a file template/__init__.py in the root directory of this repo and override settings from defaults/ folder.


### Example configuration

Assuming there are two machines:

  - 192.168.1.90 - all in one nebula server + production storage
  - 192.168.1.91 - caspar cg playout server

```python

import socket

HOST = socket.gethostname()

from defaults import *

#
# Configured storages are mounted to /mnt/${sitename}_${idstorage}/
# By default /mnt/sitename_01/.nx/ is used to store plugins, low-res
# videos, thumbnails, reports etc.
#

data["storages"] = {
    1 : {
        "title"    : "production",
        "protocol" : "samba",
        "path"     : "//192.168.1.90/storage",
        "login"    : "nebula",
        "password" : "nebulapass"
    },

    2 : {
        "title"    : "playout",
        "protocol" : "samba",
        "path"     : "//192.168.1.91/storage",
        "login"    : "nebula",
        "password" : "nebulapass"
    }
}

#
# Currently only playout channels (type 0) are supported.
#

data["channels"] = {
    1 :  [0, {
        'title': 'Nebula TV',
        'engine' : 'casparcg',
        'controller_host' : 'localhost',
        'controller_port' : 42100,
        'caspar_host' : '192.168.1.90',
        'caspar_port' : 5250,
        'caspar_channel' : 1,
        'caspar_feed_layer' : 10,
        'playout_storage' : 2,
        'playout_dir' : "media.dir",
        'playout_container' : 'mov',
        'day_start' : [8, 0],
        'send_action' : 2,
        'rundown_accepts': "asset['content_type'] == VIDEO",
        'scheduler_accepts': "asset['id_folder'] in [1, 2]",
        'fps': 25,
        'live_source' : 'DECKLINK 2 FORMAT 1080i5000',
        'plugins': [],
    }]
}

data["services"] = {
    1  : ["mesg",   HOST, "mesg",    "template/services/mesg.xml",  True, 5],
    2  : ["broker", HOST, "broker",  None,                          True, 5],
    3  : ["meta",   HOST, "meta",    None,                          True, 5],
    4  : ["play",   HOST, "play",    "template/services/play.xml",  True, 5],
    5  : ["conv",   HOST, "conv01",  None,                          True, 5],
    6  : ["psm",    HOST, "psm",     None,                          True, 30],
}

```

Services
--------

### mesg

Messaging/logging

### play

Playout controller

### broker

Jobs broker

### meta

Metadata extraction service

### conv

Media transcoding service

### psm

Playout storage monitor

### watch

Watchfolder service.
