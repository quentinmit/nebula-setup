--
-- SYSTEM SETTINGS
--

CREATE TABLE public.settings (
        key VARCHAR(255) NOT NULL,
        value VARCHAR(255),
        CONSTRAINT settings_pkey PRIMARY KEY (key)
    );

CREATE TABLE public.channels (
        id SERIAL NOT NULL,
        title VARCHAR(255) NOT NULL,
        channel_type INTEGER NOT NULL,
        settings JSONB NOT NULL,
        CONSTRAINT channels_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.storages (
        id serial NOT NULL,
        title VARCHAR(50) NOT NULL,
        protocol INTEGER NOT NULL,
        path VARCHAR(255) NOT NULL,
        login VARCHAR(50),
        password VARCHAR(50),
        CONSTRAINT storages_pkey PRIMARY KEY (id)
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

CREATE TABLE public.users (
        id SERIAL NOT NULL,
        login VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        metadata JSONB,
        CONSTRAINT users_pkey PRIMARY KEY (id)
    );

--
-- MAM SETTINGS
--

CREATE TABLE public.views (
        id SERIAL NOT NULL,
        title VARCHAR(255) NOT NULL,
        settings XML NOT NULL,
        owner INTEGER NOT NULL DEFAULT 0,
        position INTEGER NOT NULL DEFAULT 0,
        CONSTRAINT views_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.folders (
        id SERIAL NOT NULL,
        title VARCHAR(255),
        color INTEGER,
        meta_set JSONB,
        CONSTRAINT folders_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.origins (
        id SERIAL NOT NULL,
        title VARCHAR(255),
        CONSTRAINT origins_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.actions (
        id SERIAL NOT NULL,
        title varchar(50) NOT NULL,
        settings XML NOT NULL,
        CONSTRAINT actions_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.meta_types (
        key VARCHAR(127) NOT NULL,
        ns VARCHAR(10) NOT NULL,
        editable BOOLEAN NOT NULL,
        searchable BOOLEAN NOT NULL,
        class INTEGER NOT NULL,
        settings JSONB,
        CONSTRAINT meta_types_pkey PRIMARY KEY (key)
    );

CREATE TABLE public.meta_aliases (
        key VARCHAR(50) REFERENCES public.meta_types(key),
        lang VARCHAR(50) NOT NULL,
        alias VARCHAR(50) NOT NULL,
        col_header VARCHAR(50) NULL,
        CONSTRAINT meta_aliases_pkey PRIMARY KEY (key, lang)
    );

CREATE TABLE public.cs (
        cs varchar(50) NOT NULL,
        value varchar(255) NOT NULL,
        label varchar(255),
        position INTEGER NOT NULL DEFAULT 50,
        CONSTRAINT cs_pkey PRIMARY KEY (cs, value)
    );

--
-- MAM OBJECTS
--

CREATE TABLE public.assets (
        id SERIAL NOT NULL,
        id_folder INTEGER NOT NULL,
        id_origin INTEGER NOT NULL,
        version_of INTEGER,
        media_type INTEGER NOT NULL,
        content_type INTEGER NOT NULL,
        status INTEGER NOT NULL,
        metadata JSONB,
        ft_index TEXT,
        CONSTRAINT assets_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.bins(
        id SERIAL NOT NULL,
        bin_type INTEGER NOT NULL,
        metadata JSONB,
        CONSTRAINT bins_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.events(
        id SERIAL NOT NULL,
        event_type INTEGER NOT NULL,
        start_time INTEGER NOT NULL,
        end_time INTEGER,
        id_magic INTEGER NOT NULL,
        metadata JSONB,
        CONSTRAINT events_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.items(
        id SERIAL NOT NULL,
        id_bin INTEGER REFERENCES public.bins(id),
        id_asset INTEGER REFERENCES public.assets(id),
        position INTEGER NOT NULL,
        metadata JSONB,
        CONSTRAINT items_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.jobs (
        id serial NOT NULL,
        id_asset INTEGER NOT NULL,
        id_action INTEGER NOT NULL,
        settings JSONB NULL,
        id_user INTEGER,
        id_service INTEGER,
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
        id_channel INTEGER NOT NULL,
        id_item INTEGER REFERENCES public.items(id),
        id_asset INTEGER REFERENCES public.assets(id),
        title VARCHAR(255) NOT NULL,
        start FLOAT NOT NULL,
        stop FLOAT NOT NULL,
        CONSTRAINT asrun_pkey PRIMARY KEY (id)
    );
