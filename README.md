Nebula setup
============

Nebula installers and configuration tools.

This document describes basic Nebula installation and configuration process. Advanced techniques such as
database configuration, optimization, and backup, security, GPU acceleration support etc. are out of the scope of this guide.
For production deployment, you should get familiar with Linux security, PostgreSQL, memcached and NGINX configuration
as well as basic Python programming.

Nebula is a complex software, which can be configured to fit many different workflows, so don't be ashamed
to [get in touch with us](mailto:support@nebulabroadcast.com) and get a professional support.

Yes. This is what we do for a living.

Terms and definitions
---------------------

 - `asset` - A record in MAM database. Asset can be a physical media file, URL or just a virtual record for short text stories.
 - `folder` - Each asset falls into one folder based on its purpose (movie, music video, trailer, news story etc).
    Each folder has its own metadata set.
 - `item`
 - `bin` - Ordered list of items. Typically a playlist block.
 - `event` - Calendar record. Typically a singe program block in channel's EPG
 - `hub` - Nebula API server
 - `service` - Services are started and operated by the master process and can be controlled (stopped, restarted ) using API.
 - `plugin` - Python script which extends default Nebula functionality. There are several types of plugins available.
 - `site` - Nebula instance with own database. Usually a television network with one or more channels
 - `storage` - Nebula does not use UNC paths for access to files. Instead each storage is mounted according to its type and storage ID and relative path is used.

Prerequisites
-------------

Use `prerequisites.sh` script to install all required libraries and software

## NGINX

Nebula also needs NGINX server with http push module  and mp4 module to be installed.
Use [install.nginx.sh](https://github.com/immstudios/installers/blob/master/install.ffmpeg.sh)
and create `/var/www/yoursitename/http.conf` file.

Assuming your site name is "nebula" and NGINX server is running on the same
machine as Nebula itself, you may use the following configuration:

```nginx
server {
    server_name          _;
    set $nxcore_root    /mnt/nebula_01/.nx;

    add_header          Access-Control-Allow-Headers    'origin, content-type, accept, user-agent, referer' always;
    add_header          Access-Control-Allow-Origin     '*' always;


    location /msg_publish {
        push_stream_publisher;
        push_stream_channels_path              $arg_id;
        set $push_stream_channel_id            $arg_id;
    }

    location ~ /ws/(.*) {
        push_stream_subscriber                 websocket;
        push_stream_channels_path              $1;
        push_stream_ping_message_interval      10s;
    }

    location /proxy/ {
        mp4;
        mp4_max_buffer_size 5m;
        root                $nxcore_root;
    }

    location / {
        proxy_pass          http://localhost:8080;
        proxy_set_header    Host $host;
        proxy_set_header    X-Real-IP $remote_addr;
    }
}
```

:warning: *This is just a very simple configuration example. Always use https in production!*


## FFMpeg

Conversion nodes depend on ffmpeg. You may use
[this script](https://github.com/immstudios/installers/blob/master/install.ffmpeg.sh)
to install it.


Site template
-------------

Create a file `template/__init__.py` in the root directory of this repository to override settings from `defaults/` folder.


### Example configuration

Assuming there are two machines:

  - **192.168.1.90** - all in one nebula server + production storage
  - **192.168.1.91** - caspar cg playout server

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
        'solvers': [],
        'meta_set' : [
                ('title', {}),
                ('description', {})
            ]
    }]
}


#
# Services
#

#         type      host  title      config path                    autostart  loop_delay

data["services"] = {
    1  : ["mesg",   HOST, "mesg",    "template/services/mesg.xml",  True,      5],
    2  : ["broker", HOST, "broker",  None,                          True,      5],
    3  : ["meta",   HOST, "meta",    None,                          True,      5],
    4  : ["play",   HOST, "play",    "template/services/play.xml",  True,      5],
    5  : ["conv",   HOST, "conv01",  None,                          True,      5],
    6  : ["psm",    HOST, "psm",     None,                          True,      30],
}

```

Services
--------

### mesg

Messaging/logging service. One is needed for each network segment.

Relay address is the address of the configured NGINX server.
All multicast status messages will be relayed to its HTTP push module and served to clients
using websockets.

```xml
<service>
    <relay>http://192.168.32.2</relay>
    <log_dir>/var/log/nebula</log_dir>
</service>
```

### play

Playout controller.

Only `id_channel` parameter must be specified in the service configuration.
There must not be two services controlling the same channel at the same time!

```xml
<settings>
    <id_channel>1</id_channel>
</settings>
```

### broker

Jobs broker. One **broker** service is needed per site. No configuration file is needed.

### meta

Metadata extraction service. Two meta services are recommended for each site.
One with no configuration file at all (scan all files) and one with the following configuration:

```xml
<settings>
    <cond>asset["status"] == CREATING</cond>
</settings>
```

This one will scan only recently changed media files, which significantly improves overal system performance.

### conv

Media transcoding service. A configuration file is optional and allows to limit service usage to
perform a particular action(s).

### psm

Playout storage monitor. One **psm** service is needed if the site uses one or more playout channels.
No configuration file is needed.

### watch

Watchfolder service creates new assets from media files.

Folder tag attributes:

 - `id_storage` (required)
 - `path` (required)
 - `id_folder` (default  12 - Incoming)
 - `recursive` (default True)
 - `hidden` (default False) - Ignore dotfiles
 - `quarantine_time` (default 10)
 - `case_sensitive_exts` (default False)

```xml
<service>
    <folder id_storage="1" path="media.dir"></folder>
</service>
```
### worker

Worker is a wrapper service, which executes given worker plugin script.

Configuration example:

```xml
<service script="dummy"/>
```

### Analyzer

Advanced content analysis. This service is not yet finished and its configuration
is subject of changes.

### Import

File ingest services based on Themis library. This service is not yet finished and its configuration
is subject of changes.
