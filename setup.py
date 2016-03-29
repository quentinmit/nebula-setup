#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys
import time
import json


#
# Env setup
#

if sys.version_info[:2] < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf-8')

nebula_root = os.path.abspath(os.getcwd())

#
# Vendor imports
#

vendor_dir = os.path.join(nebula_root, "vendor")
if os.path.exists(vendor_dir):
    for pname in os.listdir(vendor_dir):
        pname = os.path.join(vendor_dir, pname)
        pname = os.path.abspath(pname)
        if not pname in sys.path:
            sys.path.insert(0, pname)

from nebula import *
from nebula.template_meta import BASE_META_SET

config["nebula_root"] = nebula_root


def clear_settings():
    logging.info("Removing settings")
    db = DB()
    db.query("""
        TRUNCATE TABLE
            cs,
            folders,
            actions,
            channels,
            services,
            settings,
            storages,
            views,
            origins
        RESTART IDENTITY CASCADE;""")
    db.commit()


def clear_objects():
    logging.info("Removing all objects")
    db = DB()
    db.query("""
        TRUNCATE TABLE
            assets,
            items,
            bins,
            events,
            users,
            jobs,
            asrun
        RESTART IDENTITY;""")
    db.commit()


def clear_all():
    clear_objects()
    clear_settings()



def create_core():
    db = DB()
    for id, title in [[1, "Production"]]:
        db.query(
            "INSERT INTO origins (id, title) VALUES (%s, %s)",
            [id, title]
            )

    for ns, key, e, f, cl, settings in BASE_META_SET:
        if settings:
            settings = json.dumps(settings)
        db.query(
                "INSERT INTO meta_types (key, ns, editable, searchable, class, settings) VALUES (%s, %s, %s, %s, %s, %s)",
                [key, ns, bool(e), bool(f), cl, settings]
                )

#    for key, lang, alias, col_header in BASE_META_ALIASES:
#        pass
    db.commit()



def migrate(data):
    """Transfer Nebula4 data dump to v5 database"""
    start_time = time.time()
    db = DB()

    for cs, value, label in data["cs"]:
        db.query(
            "INSERT INTO cs (cs, value, label) VALUES (%s, %s, %s)",
            [cs, value, label]
            )

    for key, value in data["settings"]:
        db.query(
            "INSERT INTO settings (key, value) VALUES (%s, %s)",
            [key, value]
            )


    max_id = 0
    for id_folder, title, color, meta_set, validator in data["folders"]:
        db.query(
            "INSERT INTO folders (id, title, color, meta_set) VALUES (%s, %s, %s, %s)",
            [id_folder, title, color, meta_set]
            )
        max_id = max(id_folder, max_id)
    db.query("ALTER SEQUENCE folders_id_seq RESTART WITH %s", [max_id + 1])


    max_id = 0
    for id_action, title, config in data["actions"]:
        db.query(
            "INSERT INTO actions (id, title, settings) VALUES (%s, %s, %s)",
            [id_action, title, config]
            )
        max_id = max(id_action, max_id)
    db.query("ALTER SEQUENCE actions_id_seq RESTART WITH %s", [max_id + 1])


    max_id = 0
    for id_channel, channel_type, title, config in data["channels"]:
        db.query(
            "INSERT INTO channels (id, title, channel_type, settings) VALUES (%s, %s, %s, %s)",
            [id_channel, title, channel_type, config]
            )
        max_id = max(id_channel, max_id)
    db.query("ALTER SEQUENCE channels_id_seq RESTART WITH %s", [max_id + 1])


    max_id = 0
    for id_service, agent, title, autostart, loop_delay, settings, state, pid, last_seen in data["services"]:
        #TODO:missing host in dump
        host="devula"
        db.query(
            "INSERT INTO services (id, agent, title, host, autostart, loop_delay, settings) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            [id_service, agent, title, host, autostart, loop_delay, settings]
            )
        max_id = max(id_service, max_id)
    db.query("ALTER SEQUENCE services_id_seq RESTART WITH %s", [max_id + 1])


    max_id = 0
    for id_storage, title, protocol, path, login, password in data["storages"]:
        db.query(
            "INSERT INTO storages (id, title, protocol, path, login, password) VALUES (%s, %s, %s, %s, %s, %s)",
            [id_storage, title, protocol, path, login, password]
            )
        max_id = max(id_storage, max_id)
    db.query("ALTER SEQUENCE storages_id_seq RESTART WITH %s", [max_id + 1])


    max_id = 0
    for id_view, title, owner, config, position in data["views"]:
        db.query(
            "INSERT INTO views (id, title, settings, owner, position) VALUES (%s, %s, %s, %s, %s)",
            [id_view, title, config, owner, position]
            )
        max_id = max(id_view, max_id)
    db.query("ALTER SEQUENCE views_id_seq RESTART WITH %s", [max_id + 1])

    #
    # Finish
    #

    db.commit()
    logging.goodnews("Nebula settings migration completed in {:03f} seconds".format(time.time() - start_time))




if __name__ == "__main__":

    dump_path = sys.argv[1] if len(sys.argv) == 2 and os.path.exists(sys.argv[1]) else "../dump.json"
    if not os.path.exists(dump_path):
        critical_error("Unable to find dump file")

    with open(dump_path) as f:
        data = json.load(f)

    clear_all()
    create_core()
    migrate(data)
