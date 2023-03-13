-- Table: operational.resource_based_service

-- DROP TABLE IF EXISTS operational.resource_based_service;

CREATE TABLE IF NOT EXISTS operational.resource_based_service(
    max_time_to_notify_us time without time zone NOT NULL,
    service_id integer NOT NULL,
    id serial NOT NULL,
    resource operational.resource_type NOT NULL,
    CONSTRAINT resource_based_service_service_id FOREIGN KEY (service_id)
        REFERENCES operational.service (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)


TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.resource_based_service
    OWNER to postgres;
