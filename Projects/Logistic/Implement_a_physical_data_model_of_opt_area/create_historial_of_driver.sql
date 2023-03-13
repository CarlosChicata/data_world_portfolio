-- Table: operational.historial_of_driver

-- DROP TABLE IF EXISTS operational.historial_of_driver;

CREATE TABLE IF NOT EXISTS operational.historial_of_driver
(
    id integer NOT NULL DEFAULT nextval('operational.historial_of_driver_id_seq'::regclass),
    start_apply timestamp without time zone NOT NULL,
    finish_apply timestamp without time zone NOT NULL,
    response operational.response,
    reason_of_response text COLLATE pg_catalog."default",
    drive_id integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    service_id integer NOT NULL,
    datetime_response timestamp without time zone,
    service_name character varying(15) COLLATE pg_catalog."default" NOT NULL,
    fullname_driver character varying(180) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT historial_of_driver_id_idx PRIMARY KEY (id),
    CONSTRAINT historial_of_driver_driver_id FOREIGN KEY (drive_id)
        REFERENCES operational.driver (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_of_driver_service_id FOREIGN KEY (service_id)
        REFERENCES operational.service (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.historial_of_driver
    OWNER to postgres;