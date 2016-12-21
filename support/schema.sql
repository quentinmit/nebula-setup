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
        settings JSONB NOT NULL,
        CONSTRAINT storages_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.channels (
        id SERIAL NOT NULL,
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
        title VARCHAR(255) NOT NULL,
        settings XML NOT NULL,
        CONSTRAINT actions_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.folders (
        id SERIAL NOT NULL,
        settings JSONB,
        CONSTRAINT folders_pkey PRIMARY KEY (id)
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

CREATE TABLE public.assets (
        id SERIAL NOT NULL,
        id_folder INTEGER NOT NULL,
        version_of INTEGER DEFAULT 0,
        ctime INTEGER NOT NULL,
        mtime INTEGER NOT NULL,
        meta JSONB,
        CONSTRAINT assets_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.bins (
        id SERIAL NOT NULL,
        bin_type INTEGER DEFAULT 0,
        ctime INTEGER NOT NULL,
        mtime INTEGER NOT NULL,
        meta JSONB,
        CONSTRAINT bins_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.items (
        id SERIAL NOT NULL,
        id_asset INTEGER REFERENCES public.assets(id),
        id_bin INTEGER REFERENCES public.bins(id),
        position INTEGER NOT NULL,
        ctime INTEGER NOT NULL,
        mtime INTEGER NOT NULL,
        meta JSONB,
        CONSTRAINT items_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.events (
        id SERIAL NOT NULL,
        id_channel INTEGER REFERENCES public.channels(id),
        start INTEGER NOT NULL,
        stop INTEGER,
        id_magic INTEGER,
        ctime INTEGER NOT NULL,
        mtime INTEGER NOT NULL,
        meta JSONB,
        CONSTRAINT events_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.users (
        id SERIAL NOT NULL,
        meta JSONB,
        ctime INTEGER NOT NULL,
        mtime INTEGER NOT NULL,
        CONSTRAINT users_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.ft (
        id INTEGER NOT NULL,
        object_type INTEGER NOT NULL,
        weight INTEGER DEFAULT 0,
        value VARCHAR(255)
    );


CREATE INDEX idx_folders ON assets(id_folder);
CREATE INDEX idx_ctime ON assets(ctime);
CREATE INDEX idx_mtime ON assets(mtime);
CREATE INDEX idx_items_bin ON items(id_bin);
CREATE INDEX idx_event_channel ON events(id_channel);
CREATE INDEX idx_event_start ON events(start);
CREATE INDEX idx_event_magic ON events(id_magic);

CREATE INDEX idx_ft_id ON ft(id);
CREATE INDEX idx_ft_type ON ft(object_type);
CREATE INDEX idx_ft ON ft(value text_pattern_ops);

--
-- AUX
--

CREATE TABLE public.jobs (
        id SERIAL NOT NULL,
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
        id_item INTEGER REFERENCES public.items(id),
        id_asset INTEGER REFERENCES public.assets(id),
        start FLOAT NOT NULL,
        stop FLOAT NOT NULL,
        CONSTRAINT asrun_pkey PRIMARY KEY (id)
    );

CREATE INDEX asrun_start_idx ON asrun(start);
CREATE INDEX asrun_channel_idx ON asrun(id_channel);
CREATE INDEX asrun_asset_idx ON asrun(id_asset);
