--
-- SYSTEM SETTINGS
--

CREATE TABLE public.settings (
        key VARCHAR(255) NOT NULL,
        value JSONB,
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
        settings JSONB NOT NULL,
        CONSTRAINT storages_pkey PRIMARY KEY (id)
    );


CREATE TABLE public.users (
        id SERIAL NOT NULL,
        login VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        meta JSONB,
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

CREATE TABLE public.asset_types (
        id SERIAL NOT NULL,
        title VARCHAR(255),
        color INTEGER DEFAULT 13421772, -- Light gray
        settings JSONB,
        CONSTRAINT asset_types_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.meta_types (
        ns VARCHAR(10) NOT NULL,
        key VARCHAR(127) NOT NULL,
        settings JSONB NOT NULL,
        CONSTRAINT meta_types_pkey PRIMARY KEY (key)
    );

CREATE TABLE public.meta_aliases (
        key VARCHAR(50) REFERENCES public.meta_types(key),
        language VARCHAR(50) NOT NULL,
        alias VARCHAR(50) NOT NULL,
        description TEXT,
        header VARCHAR(50) NULL,
        CONSTRAINT meta_aliases_pkey PRIMARY KEY (key, language)
    );

CREATE TABLE public.cs (
        cs VARCHAR(255) NOT NULL,
        key VARCHAR(255) NOT NULL,
        value JSONB NOT NULL,
        CONSTRAINT cs_pkey PRIMARY KEY (cs, value)
    );

CREATE TABLE public.cs_aliases (
        cs VARCHAR(255) NOT NULL,
        key VARCHAR(255) NOT NULL,
        language VARCHAR(10) NOT NULL,
        alias VARCHAR(255) NOT NULL,
        description TEXT,
        position INTEGER NOT NULL DEFAULT 50,
        CONSTRAINT cs_aliases_pkey PRIMARY KEY (cs, key, language)
);

--
-- MAM OBJECTS
--

CREATE TABLE public.assets (
        id SERIAL NOT NULL,
        asset_type INTEGER REFERENCES public.asset_types(id),
        origin INTEGER REFERENCES public.origins(id),
        meta JSONB,
        ft_index TEXT,
        CONSTRAINT assets_pkey PRIMARY KEY (id)
    );

CREATE INDEX idx_assets_ft ON assets(ft_index);

CREATE TABLE public.bins(
        id SERIAL NOT NULL,
        bin_type INTEGER NOT NULL,
        meta JSONB,
        CONSTRAINT bins_pkey PRIMARY KEY (id)
    );

CREATE TABLE public.events(
        id SERIAL NOT NULL,
        event_type INTEGER NOT NULL,
        start_time INTEGER NOT NULL,
        end_time INTEGER NOT NULL,
        meta JSONB,
        CONSTRAINT events_pkey PRIMARY KEY (id)
    );

CREATE INDEX idx_events_start_time ON events(start_time);
CREATE INDEX idx_events_end_time ON events(end_time);
CREATE INDEX idx_events_event_type ON events(event_type);

CREATE TABLE public.items(
        id SERIAL NOT NULL,
        id_bin INTEGER REFERENCES public.bins(id),
        id_asset INTEGER REFERENCES public.assets(id),
        position INTEGER NOT NULL,
        meta JSONB,
        CONSTRAINT items_pkey PRIMARY KEY (id)
    );








-- TODO: Clean-UP
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

-- TODO: Clean-UP
CREATE TABLE public.asrun (
        id SERIAL NOT NULL,
        id_channel INTEGER REFERENCES public.channels(id),
        id_item INTEGER REFERENCES public.items(id),
        id_asset INTEGER REFERENCES public.assets(id),
        title VARCHAR(255) NOT NULL,
        start FLOAT NOT NULL,
        stop FLOAT NOT NULL,
        CONSTRAINT asrun_pkey PRIMARY KEY (id)
    );

-- TODO: Clean-UP
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
