#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import time
import json

try:
    import psycopg2
except ImportError:
    log_traceback("Import error")
    critical_error("Unable to import psycopg2")

import rex

from nxtools import *
from templates import *

#
# Settings
#

config = {}
try:
    config.update(json.load(open("settings.json")))
except Exception:
    log_traceback("Configuration error")
    critical_error("Unable to open settings file")

#
# Database connection
#

class DB(object):
    def __init__(self, **kwargs):
        self.pmap = {
                "host" : "db_host",
                "user" : "db_user",
                "password" : "db_pass",
                "database" : "db_name",
            }

        self.settings = {
                key : kwargs.get(self.pmap[key], config[self.pmap[key]]) for key in self.pmap
            }

        self.conn = psycopg2.connect(**self.settings)
        self.cur = self.conn.cursor()

    def lastid(self):
        self.query("SELECT LASTVAL()")
        return self.fetchall()[0][0]

    def query(self, query, *args):
        self.cur.execute(query, *args)

    def fetchone(self):
        return self.cur.fetchone()

    def fetchall(self):
        return self.cur.fetchall()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.conn.close()

    def __len__(self):
        return True

#
# Template installers
#

def install_settings():
    logging.info("Installing site settings")
    db = DB()
    db.query("DELETE FROM settings")
    for key in data["settings"]:
        value = json.dumps(data["settings"][key])
        db.query("INSERT INTO settings (key, value) VALUES (%s, %s)", [key, value])
    db.commit()


def install_storages():
    logging.info("Installing storages")
    pass


def install_channels():
    logging.info("Installing channels")
    pass


def install_services():
    logging.info("Installing services")
    pass


def install_actions():
    logging.info("Installing actions")
    pass


def install_asset_types()
    logging.info("Installing asset types")
    db = DB()
    db.query("DELETE FROM asset_types")
    for id in data["asset_types"]:
        settings = data["asset_types"][id]
        title = settings["title"]
        db.query(
                "INSERT INTO asset_types (id, title, settings) VALUES (%s, %s, %s)",
                [id, title, json.dumps("settings")]
            )
    db.query("SELECT pg_catalog.setval(pg_get_serial_sequence('asset_types', 'id'), MAX(id)) FROM asset_types;")
    db.commit()


def install_meta_types():
    logging.info("Installing metadata set")
    db = DB()
    languages = ["en"]

    aliases = {}
    for lang in languages:
        aliases[lang] = {}
        trans_table_fname = os.path.join("aliases", "meta-aliases-{}.json".format(lang))
        l = json.load(open(trans_table_fname))
        for key, alias, header in l:
            aliases[lang][key] = [alias, header]

    db.query("DELETE FROM meta_types")
    for key in data["meta_types"]:
        ns, e, index, ft, cls, settings = data["meta_types"][key]
        meta_type_data = {
                "ns" : ns,
                "class" : cls,
                "fulltext" : ft,
                "editable" : e,
                "aliases" : {}
            }

        for lang in languages:
            meta_type_data["aliases"][lang] = aliases[lang][key]

        db.query(
                "INSERT INTO meta_types (key, settings) VALUES (%s, %s)",
                [key, json.dumps(meta_type_data)]
            )
        if index:
            idx_name = "idx_" + key.replace("/", "_")
            db.query(
                    "CREATE INDEX IF NOT EXISTS {} ON objects((meta->>%s))".format(idx_name),
                    [key]
                )
    db.commit()


def install_cs():
    pass


def install_views():
    pass


#
# Run
#

if __name__ == "__main__":
    start_time = time.time()

    install_settings()
    install_storages()
    install_channels()
    install_services()
    install_actions()
    install_asset_types()
    install_meta_types()
    install_cs()
    install_views()

    logging.goodnews("Nebula settings migration completed in {:03f} seconds".format(time.time() - start_time))
