import socket

HOST = socket.gethostname()

from defaults import *

data["settings"]["debug_mode"] = True

#
# Configured storages are mounted to /mnt/${sitename}_${idstorage}/
# By default /mnt/sitename_01/.nx/ is used to store plugins, low-res
# videos, thumbnails, reports etc.
#

import keyring

data["storages"] = {
    1 : {
        "title"    : "sctv-nas",
        "protocol" : "samba",
        "path"     : "//sctv-nas.mit.edu/Multimedia",
        "login"    : "nebula",
    },
    2 : {
        "title"    : "sctv-firefly",
        "protocol" : "samba",
        "path"     : "//sctv-firefly.mit.edu/Multimedia",
        "login"    : "nebula",
    },
}
for v in data['storages'].values():
    if 'password' not in v:
        v['password'] = keyring.get_password('smb:' + v['path'], v['login'])

#
# Currently only playout channels (type 0) are supported.
#

data["channels"] = {
    1 :  [0, {
        'title': 'MITV 36',
        'engine' : 'vlc',
        'controller_host' : '172.25.89.2',
        'controller_port' : 42100,
        'caspar_feed_layer' : 10,
        'playout_storage' : 1,
        'playout_dir' : ".nx/playout",
        'playout_container' : 'mov',
        'day_start' : [8, 0],
#        'send_action' : 2,
        'rundown_accepts': "asset['content_type'] == VIDEO",
        'scheduler_accepts': "asset['id_folder'] in [1, 2]",
        'fps': 30,
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

#         type      host                  title      config path                    autostart  loop_delay

data["services"] = {
    1  : ["mesg",   "sctv-television-rx", "mesg",    "template/services/mesg.xml",  True,      5],
    2  : ["broker", "sctv-television-rx", "broker",  None,                          True,      5],
    3  : ["meta",   "sctv-television-rx", "meta",    None,                          True,      5],
    4  : ["play",   "sctv-playout",       "play",    "template/services/play.xml",  False,     5],
    5  : ["conv",   "sctv-television-rx", "conv01",  None,                          True,      5],
    6  : ["psm",    "sctv-television-rx", "psm",     None,                          True,      30],
    7  : ["watch",  "sctv-television-rx", "watch sctv-nas", "template/services/watch-sctv-nas.xml", True, 5],
}

#
# Actions
#

#         title         type    config path
data["actions"] = {
    1  : ["Make proxy", "conv", "template/actions/proxy.xml"],
}
