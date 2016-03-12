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
        title varchar(50) NOT NULL,
        protocol integer NOT NULL,
        path varchar(255) NOT NULL,
        login varchar(50) NOT NULL,
        password varchar(50) NOT NULL,
        CONSTRAINT storages_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.services (
        id SERIAL NOT NULL,
        agent VARCHAR(50) NOT NULL,
        title VARCHAR(50) NOT NULL,
        host VARCHAR(50) NOT NULL,
        autostart INTEGER NOT NULL,
        loop_delay INTEGER NOT NULL,
        settings TEXT NULL,
        state INTEGER NOT NULL,
        pid INTEGER NOT NULL,
        last_seen INTEGER NOT NULL,
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
        settings JSONB NOT NULL,
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
        settings text NOT NULL,
        CONSTRAINT actions_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.meta_types (
        key VARCHAR(127) NOT NULL,
        ns VARCHAR(10) NOT NULL,
        editable BOOLEAN NOT NULL,
        searchable BOOLEAN NOT NULL,
        class INTEGER NOT NULL,
        settings JSONB NOT NULL,
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
        CONSTRAINT cs_pkey PRIMARY KEY (cs, value)
    );

--
-- MAM OBJECTS
--

CREATE TABLE public.assets (
        id SERIAL NOT NULL,
        id_folder INTEGER REFERENCES public.folders(id),
        id_origin INTEGER REFERENCES public.origins(id),
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
        end_time INTEGER NOT NULL,
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
        settings TEXT NULL,
        id_user INTEGER NOT NULL,
        id_service INTEGER NOT NULL,
        progress INTEGER NOT NULL,
        message TEXT NOT NULL,
        priority INTEGER NOT NULL,
        retries INTEGER NOT NULL,
        creation_time INTEGER NOT NULL,
        start_time INTEGER NOT NULL,
        end_time INTEGER NOT NULL,
        CONSTRAINT jobs_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.asrun (
        id SERIAL NOT NULL,
        id_channel INTEGER NOT NULL,
        start INTEGER NOT NULL,
        stop INTEGER NOT NULL,
        title VARCHAR(255) NOT NULL,
        id_item INTEGER NOT NULL,
        id_asset INTEGER NOT NULL,
        CONSTRAINT asrun_pkey PRIMARY KEY (id)
    );
