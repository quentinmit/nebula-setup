from .core import *
from .db import DB

__all__ = ["clear_settings", "clear_objects", "clear_all", "insert"]

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
            meta_types,
            meta_aliases
        RESTART IDENTITY;""")
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


def insert(db, table, **kwargs):
    keys = kwargs.keys()
    values = [kwargs[key] for key in keys]
    keys = [key.rstrip("_") for key in keys]
    q = "INSERT INTO {} ({}) VALUES ({})".format(table, ", ".join(keys), ", ".join(["%s"] * len(keys)))
    db.query(q, values)
