-- Table: operational.service

-- DROP TABLE IF EXISTS operational.service;

CREATE TABLE IF NOT EXISTS operational.service
(
    name character varying(15) COLLATE pg_catalog."default" NOT NULL,
    id integer NOT NULL DEFAULT nextval('operational.service_id_seq'::regclass),
    type operational.resource_type NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    is_limite_time boolean NOT NULL DEFAULT false,
    min_hours time without time zone,
    max_hours time without time zone,
    use_crossdocking boolean NOT NULL DEFAULT false,
    has_work_sundays boolean NOT NULL DEFAULT false,
    has_work_holidays boolean NOT NULL DEFAULT false,
    limite_time_to_delivery json,
    applied_vehicle_to_use operational.vehicle_type[],
    resource operational.resource_type NOT NULL,
    max_time_to_notify_us time without time zone NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT service_id_idx PRIMARY KEY (id),
    CONSTRAINT service_name_unique UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.service
    OWNER to postgres;