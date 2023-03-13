-- Table: operational.request_of_vehicle

-- DROP TABLE IF EXISTS operational.request_of_vehicle;

CREATE TABLE IF NOT EXISTS operational.request_of_vehicle
(
    request_id integer NOT NULL,
    vehicle_id integer NOT NULL,
    CONSTRAINT request_of_vehicle_vehicle_id FOREIGN KEY (vehicle_id)
        REFERENCES operational.vehicle (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT request_of_vehicle_request_id FOREIGN KEY (request_id)
        REFERENCES operational.request (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.request_of_vehicle
    OWNER to postgres;
