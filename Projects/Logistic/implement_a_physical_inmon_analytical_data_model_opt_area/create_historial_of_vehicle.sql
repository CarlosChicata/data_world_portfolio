-- Table: operational.historial_of_vehicle

-- DROP TABLE IF EXISTS operational.historial_of_vehicle;

CREATE TABLE IF NOT EXISTS operational.historial_of_vehicle
(
    historial_event_id integer NOT NULL,
    cost_of_usage money NOT NULL,
    status_of_finish_operation operational.vehicle_status NOT NULL,
    cost_of_repair money,
    vehicle_id integer NOT NULL,
    driver_id integer NOT NULL,
    datetime_of_paid_repair timestamp without time zone,
    CONSTRAINT historial_of_vehicle_driver_id FOREIGN KEY (driver_id)
        REFERENCES operational.driver (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_of_vehicle_event_id FOREIGN KEY (historial_event_id)
        REFERENCES operational.historial_event (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_of_vehicle_vehicle_id FOREIGN KEY (vehicle_id)
        REFERENCES operational.vehicle (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.historial_of_vehicle
    OWNER to postgres;