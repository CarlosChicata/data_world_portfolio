-- Table: operational.historial_of_driver

-- DROP TABLE IF EXISTS operational.historial_of_driver;

CREATE TABLE IF NOT EXISTS operational.historial_of_driver
(
    historial_event_id integer NOT NULL,
    drive_id integer NOT NULL,
    service_id integer NOT NULL,
    fullname_driver character varying(180) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT historial_of_driver_driver_id FOREIGN KEY (drive_id)
        REFERENCES operational.driver (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_of_vehicle_event_id FOREIGN KEY (historial_event_id)
        REFERENCES operational.historial_event (id_register) MATCH SIMPLE
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