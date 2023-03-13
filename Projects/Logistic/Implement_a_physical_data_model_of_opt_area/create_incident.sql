-- Table: operational.incident

-- DROP TABLE IF EXISTS operational.incident;

CREATE TABLE IF NOT EXISTS operational.incident
(
    id integer NOT NULL DEFAULT nextval('operational.incident_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    responsability operational.incident_responsibility NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    apply_discount_in_driver boolean NOT NULL DEFAULT false,
    discount_operator_of_driver operational.incentive_operation,
    discount_value_of_driver real,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    CONSTRAINT incident_id_idx PRIMARY KEY (id),
    CONSTRAINT name UNIQUE (name),
    CONSTRAINT incident_consistency_discount CHECK (
CASE
    WHEN discount_operator_of_driver IS NOT NULL AND discount_value_of_driver IS NULL THEN false
    WHEN discount_operator_of_driver IS NULL AND discount_value_of_driver IS NOT NULL THEN false
    ELSE true
END)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.incident
    OWNER to postgres;