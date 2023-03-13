-- Table: operational.Enterprise

-- DROP TABLE IF EXISTS operational."Enterprise";

CREATE TABLE IF NOT EXISTS operational.enterprise
(
    id_register integer NOT NULL,
    commercial_name character varying(80) COLLATE pg_catalog."default" NOT NULL,
    business_name character varying(40) COLLATE pg_catalog."default" NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT enterprise_id_idx PRIMARY KEY (id_register)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational."Enterprise"
    OWNER to postgres;