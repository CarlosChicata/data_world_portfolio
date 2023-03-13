-- Table: operational.vehicle_in_order_based_service

-- DROP TABLE IF EXISTS operational.vehicle_in_order_based_service;

CREATE TABLE IF NOT EXISTS operational.vehicle_in_order_based_service(
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    vehicle operational.vehicle_type,
    id serial NOT NULL,
    order_based_service_id integer NOT NULL,
    CONSTRAINT vehicle_in_order_based_service_service_id FOREIGN KEY (order_based_service_id)
        REFERENCES operational.order_based_service (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)


TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.vehicle_in_order_based_service
    OWNER to postgres;

