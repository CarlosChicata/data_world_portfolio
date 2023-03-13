-- Table: operational.resource_vehicle

-- DROP TABLE IF EXISTS operational.resource_vehicle;

CREATE TABLE IF NOT EXISTS operational.resource_vehicle
(
    id_internal serial NOT NULL,
    vehicle_id integer NOT NULL,
    historial_of_warehouse_moving_id integer NOT NULL,
    CONSTRAINT resource_shipment_id_idx PRIMARY KEY (id_internal),
    CONSTRAINT resource_shipment_vehicle_id FOREIGN KEY (vehicle_id)
        REFERENCES operational.vehicle (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT resource_shipment_historial_of_warehouse_moving_id FOREIGN KEY (historial_of_warehouse_moving_id)
        REFERENCES operational.historial_warehouse_in_moving_resource (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.resource_vehicle
    OWNER to postgres;
