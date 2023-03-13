-- Table: operational.driver

-- DROP TABLE IF EXISTS operational.driver;

CREATE TABLE IF NOT EXISTS operational.driver
(
    "SOAT_deadline" date NOT NULL,
    "SOAT_number" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    license_driver_deadline date NOT NULL,
    license_driver_number character varying(20) COLLATE pg_catalog."default" NOT NULL,
    has_license_driver boolean NOT NULL,
    has_own_vehicle boolean NOT NULL DEFAULT true,
    use_internal_vehicle boolean NOT NULL DEFAULT false,
    id integer NOT NULL,
    period_of_pay int4range NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    CONSTRAINT driver_id_idx PRIMARY KEY (id),
    CONSTRAINT driver_use_id FOREIGN KEY (id)
        REFERENCES operational."user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.driver
    OWNER to postgres;