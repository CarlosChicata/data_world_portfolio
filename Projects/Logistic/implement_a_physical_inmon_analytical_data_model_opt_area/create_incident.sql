-- Table: operational.incident

-- DROP TABLE IF EXISTS operational.incident;

CREATE TABLE IF NOT EXISTS operational.incident
(
    id_register integer NOT NULL,
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    responsability operational.incident_responsibility NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    apply_discount_in_driver boolean NOT NULL DEFAULT false,
    discount_operator_of_driver operational.incentive_operation,
    discount_value_of_driver real,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    id_internal serial NOT NULL,
    CONSTRAINT incident_id_idx PRIMARY KEY (id_register)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.incident
    OWNER to postgres;

-- Index: incident_btreae_code

-- DROP INDEX IF EXISTS operational.incident_btreae_code;

CREATE INDEX IF NOT EXISTS incident_btreae_code
    ON operational.incident USING btree
    (id_internal ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.incident
    CLUSTER ON incident_btreae_code;