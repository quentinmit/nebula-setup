--
-- SYSTEM SETTINGS
--

CREATE TABLE public.settings (
        key VARCHAR(255) NOT NULL,
        value JSONB,
        CONSTRAINT settings_pkey PRIMARY KEY (key)
    );

CREATE TABLE public.storages (
        id serial NOT NULL,
        title VARCHAR(50) NOT NULL,
        settings JSONB NOT NULL,
        CONSTRAINT storages_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.channels (
        id SERIAL NOT NULL,
        title VARCHAR(255) NOT NULL,
        channel_type INTEGER NOT NULL,
        settings JSONB NOT NULL,
        CONSTRAINT channels_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.services (
        id SERIAL NOT NULL,
        agent VARCHAR(50) NOT NULL,
        title VARCHAR(50) NOT NULL,
        host VARCHAR(50) NOT NULL,
        autostart INTEGER NOT NULL DEFAULT 0,
        loop_delay INTEGER NOT NULL DEFAULT 5,
        settings XML NULL,
        state INTEGER NOT NULL DEFAULT 0,
        pid INTEGER NOT NULL DEFAULT 0,
        last_seen INTEGER NOT NULL DEFAULT 0,
        CONSTRAINT services_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.actions (
        id SERIAL NOT NULL,
        title varchar(50) NOT NULL,
        settings XML NOT NULL,
        CONSTRAINT actions_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.asset_types (
        id SERIAL NOT NULL,
        title VARCHAR(255),
        settings JSONB,
        CONSTRAINT asset_types_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.meta_types (
        key VARCHAR(127) NOT NULL,
        settings JSONB NOT NULL,
        CONSTRAINT meta_types_pkey PRIMARY KEY (key)
    );

CREATE TABLE public.cs (
        cs VARCHAR(255) NOT NULL,
        key VARCHAR(255) NOT NULL,
        value JSONB NOT NULL,
        settings JSONB,
        CONSTRAINT cs_pkey PRIMARY KEY (cs, value)
    );

CREATE TABLE public.views (
        id SERIAL NOT NULL,
        title VARCHAR(255) NOT NULL,
        settings XML NOT NULL,
        owner INTEGER NOT NULL DEFAULT 0,
        position INTEGER NOT NULL DEFAULT 0,
        CONSTRAINT views_pkey PRIMARY KEY (id)
    );

--
-- MAM
--

CREATE TABLE public.objects (
        id SERIAL NOT NULL,
        object_type INTEGER NOT NULL,
        meta JSONB,
        CONSTRAINT assets_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.ft(
        id INTEGER NOT NULL,
        weight INTEGER DEFAULT 0,
        value TEXT NOT NULL
    );

CREATE INDEX ft_index ON ft(value text_pattern_ops);

CREATE VIEW public.assets AS SELECT id, meta FROM objects WHERE object_type = 0;
CREATE VIEW public.items  AS SELECT id, meta FROM objects WHERE object_type = 1;
CREATE VIEW public.bins   AS SELECT id, meta FROM objects WHERE object_type = 2;
CREATE VIEW public.events AS SELECT id, meta FROM objects WHERE object_type = 3;
CREATE VIEW public.users  AS SELECT id, meta FROM objects WHERE object_type = 4;

--
-- AUX
--


CREATE TABLE public.jobs (
        id serial NOT NULL,
        description JSONB NULL,
        progress INTEGER NOT NULL DEFAULT -1,
        message TEXT NOT NULL DEFAULT 'Pending',
        priority INTEGER NOT NULL DEFAULT 3,
        retries INTEGER NOT NULL DEFAULT 0,
        creation_time INTEGER,
        start_time INTEGER,
        end_time INTEGER,
        CONSTRAINT jobs_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.asrun (
        id SERIAL NOT NULL,
        id_channel INTEGER REFERENCES public.channels(id),
        id_item INTEGER REFERENCES public.objects(id),
        id_asset INTEGER REFERENCES public.objects(id),
        start FLOAT NOT NULL,
        stop FLOAT NOT NULL,
        CONSTRAINT asrun_pkey PRIMARY KEY (id)
    );
