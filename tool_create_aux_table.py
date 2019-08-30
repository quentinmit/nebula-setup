#!/usr/bin/env python3

from setup import DB

db = DB()

db.query("""
CREATE TABLE public.aux (
        id SERIAL NOT NULL,
        key VARCHAR(255) NOT NULL,
        object_type INTEGER DEFAULT 0,
        id_object INTEGER DEFAULT 0,
        data JSONB,
        CONSTRAINT aux_pkey PRIMARY KEY (id)
)

""");
db.query("CREATE INDEX aux_key ON aux(key);")
db.query("CREATE INDEX aux_object_type ON aux(object_type);")
db.query("CREATE INDEX aux_id_object ON aux(id_object);")
db.commit()
