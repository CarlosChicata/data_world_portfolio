-- Table: operational.resource_shipment

-- DROP TABLE IF EXISTS operational.resource_shipment;

CREATE TABLE IF NOT EXISTS operational.resource_shipment
(
    id_internal serial NOT NULL,
    shipment_id integer NOT NULL,
    historial_of_warehouse_moving_id integer NOT NULL,
    CONSTRAINT resource_shipment_id_idx PRIMARY KEY (id_internal),
    CONSTRAINT resource_shipment_shipment_id FOREIGN KEY (shipment_id)
        REFERENCES operational.shipment (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT resource_shipment_historial_of_warehouse_moving_id FOREIGN KEY (historial_of_warehouse_moving_id)
        REFERENCES operational.historial_warehouse_in_moving_resource (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.resource_shipment
    OWNER to postgres;

