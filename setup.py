#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys
import time
import json

##
# Env setup
##

if sys.version_info[:2] < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf-8')

nebula_root = os.path.abspath(os.getcwd())

##
# Vendor imports
##

vendor_dir = os.path.join(nebula_root, "vendor")
if os.path.exists(vendor_dir):
    for pname in os.listdir(vendor_dir):
        pname = os.path.join(vendor_dir, pname)
        pname = os.path.abspath(pname)
        if not pname in sys.path:
            sys.path.insert(0, pname)

from nebula import *
config["nebula_root"] = nebula_root


db = DB()



start_time = time.time()

#
# Open dump
#

with open("dump.json") as f:
    data = json.load(f)

#
# Site settings
#

folders = [
    [1, "Movie"],
    [2, "Serie"],
    [3, "Trailer"],
    [4, "Jingle"],
    [5, "Music"],
    [6, "News"],
    [7, "Fill"],
    [8, "Template"],
    [9, "Commercial"],
    [10, "Incomming"]
]

origins = [
    [1, "Production"],
    [2, "Playout 1"]
]

meta_types = [
]

#
# Delete everything first
#

db = DB()
db.query("""
    TRUNCATE TABLE
        folders,
        assets,
        items,
        events,
        bins,
        origins
    RESTART IDENTITY;""")
db.commit()

#
# Settings tables deployment
#

for id, title in origins:
    db.query("INSERT INTO origins (id, title) VALUES (%s, %s)", [id, title])

db.commit()







def migrate(data):
    """Transfer Nebula4 data dump to v5 database"""
    db = DB()

    for cs, value, label in data["cs"]:
        db.query("INSERT INTO cs (cs, value, label) VALUES (%s, %s, %s)", [cs, value, label])

    for id_folder, title, color, meta_set, validator in data["folders"]:
        db.query("INSERT INTO folders (id, title, color, meta_test) VALUES (%s, %s, %s, %s)", [id_folder, title, color, meta_test])

    for id_action, title, config in data["actions"]:
        pass

    for id_channel, channel_type, title, config in data["channels"]:
        pass

    for id_service, agent, title host, autostart, loop_delay, settings, state, pid, last_seen in data["services"]:
        pass

    for key, value in data["settings"]:
        pass

    for id_storage, title, protocol, path, login, password in data["storages"]:
        pass

    for id_view, title, owner, config, position in data["views"]:
        pass

    return

    logging.goodnews("Nebula migration completed in {:03f} seconds".format(time.time() - start_time))


migrate ("dump.json")"

