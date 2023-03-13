-- Table: operational.historial_of_vehicle

-- DROP TABLE IF EXISTS operational.historial_of_vehicle;

CREATE TABLE IF NOT EXISTS operational.historial_of_vehicle
(
    id integer NOT NULL DEFAULT nextval('operational.historial_of_vehicle_id_seq'::regclass),
    creation timestamp without time zone NOT NULL DEFAULT now(),
    start_apply timestamp without time zone NOT NULL,
    finish_apply timestamp without time zone NOT NULL,
    cost_of_usage money NOT NULL,
    status_of_finish_operation operational.vehicle_status NOT NULL,
    cost_of_repair money,
    response operational.response,
    reason_of_reponse text COLLATE pg_catalog."default",
    vehicle_id integer NOT NULL,
    driver_id integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    datetime_of_paid_repair timestamp without time zone,
    CONSTRAINT historial_of_vehicle_id_idx PRIMARY KEY (id),
    CONSTRAINT historial_of_vehicle_driver_id FOREIGN KEY (driver_id)
        REFERENCES operational.driver (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_of_vehicle_vehicle_id FOREIGN KEY (vehicle_id)
        REFERENCES operational.vehicle (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.historial_of_vehicle
    OWNER to postgres;