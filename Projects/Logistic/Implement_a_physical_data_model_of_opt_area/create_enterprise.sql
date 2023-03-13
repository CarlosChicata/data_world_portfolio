-- Table: operational.Enterprise

-- DROP TABLE IF EXISTS operational."Enterprise";

CREATE TABLE IF NOT EXISTS operational.enterprise
(
    id serial NOT NULL,
    commercial_name character varying(80) COLLATE pg_catalog."default" NOT NULL,
    business_name character varying(40) COLLATE pg_catalog."default" NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT enterprise_id_idx PRIMARY KEY (id),
    CONSTRAINT enterprise_bus_name_unique UNIQUE (business_name),
    CONSTRAINT enterprise_com_name_unique UNIQUE (commercial_name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational."Enterprise"
    OWNER to postgres;