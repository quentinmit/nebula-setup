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

config["nebula_root"] = nebula_root


def create_core(data):

    db = DB()
    start_time = time.time()

    #
    # Metadata set
    #

    logging.info("Installing metadata set")

    for key in data["meta_types"]:
        ns, editable, fulltext, index, class_, settings = data["meta_types"][key]
        insert(db, "meta_types",
            key=key,
            ns=ns,
            editable=bool(editable),
            searchable=bool(fulltext),
            class_=class_,
            settings=json.dumps(settings) if settings else None
            )

        if index:
            idx_name = "idx_" + key.replace("/", "_")
            db.query("CREATE INDEX IF NOT EXISTS {} ON assets(( meta->>%s ))".format(idx_name), [key])

    for lang in ["en-US"]:
        trans_table_fname = os.path.join("support", "aliases-{}.json".format(lang))
        l = json.load(open(trans_table_fname))
        for key, alias, col_header in l:
            insert(db, "meta_aliases", key=key, lang=lang, alias=alias, col_header=col_header)

    #
    # Site settings
    #

    for cs, value, label in data["cs"]:
        insert(db, "cs", cs=cs, value=value, label=label)

    for key, value in data["settings"]:
        insert(db, "settings", key=key, value=value)


    max_id = 0
    for id in data["folders"]:
        title, color, meta_set = data["folders"][id]
        insert(db, "folders", id=id, title=title, color=color, meta_set=json.dumps(meta_set))
        max_id = max(id, max_id)
    db.query("ALTER SEQUENCE folders_id_seq RESTART WITH %s", [max_id + 1])


    max_id = 0
    for id, title, settings in data["actions"]:
        insert(db, "actions", id=id, title=title, settings=settings)
        max_id = max(id, max_id)
    db.query("ALTER SEQUENCE actions_id_seq RESTART WITH %s", [max_id + 1])


    max_id = 0
    for id, channel_type, title, settings in data["channels"]:
        insert(db, "channels", id=id, channel_type=channel_type, title=title, settings=settings)
        max_id = max(id, max_id)
    db.query("ALTER SEQUENCE channels_id_seq RESTART WITH %s", [max_id + 1])


    max_id = 0
    for id, host, agent, title, autostart, loop_delay, settings in data["services"]:
        insert(db, "services", id=id, agent=agent, title=title, autostart=autostart, loop_delay=loop_delay, settings=settings)
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

    #dump_path = sys.argv[1] if len(sys.argv) == 2 and os.path.exists(sys.argv[1]) else "../dump.json"
    #if not os.path.exists(dump_path):
    #    critical_error("Unable to find dump file")

    #with open(dump_path) as f:
    #    data = json.load(f)

    clear_all()
    create_core(template_data)
#    migrate(data)
