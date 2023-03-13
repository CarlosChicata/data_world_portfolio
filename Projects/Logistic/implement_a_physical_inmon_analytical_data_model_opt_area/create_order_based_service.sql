-- Table: operational.order_based_service

-- DROP TABLE IF EXISTS operational.order_based_service;

CREATE TABLE IF NOT EXISTS operational.order_based_service(
    is_limite_time boolean NOT NULL DEFAULT false,
    min_hours time without time zone,
    max_hours time without time zone,
    limite_time_to_delivery json,
    service_id integer NOT NULL,
    id serial NOT NULL,
    CONSTRAINT order_based_service_service_id FOREIGN KEY (service_id)
        REFERENCES operational.service (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)


TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.order_based_service
    OWNER to postgres;

