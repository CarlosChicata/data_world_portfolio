-- Table: operational.service

-- DROP TABLE IF EXISTS operational.service;

CREATE TABLE IF NOT EXISTS operational.service
(
    name character varying(15) COLLATE pg_catalog."default" NOT NULL,
    id_register integer NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    use_crossdocking boolean NOT NULL DEFAULT false,
    has_work_sundays boolean NOT NULL DEFAULT false,
    has_work_holidays boolean NOT NULL DEFAULT false,
    is_delete boolean NOT NULL DEFAULT false,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT service_id_idx PRIMARY KEY (id_register),
    
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.service
    OWNER to postgres;