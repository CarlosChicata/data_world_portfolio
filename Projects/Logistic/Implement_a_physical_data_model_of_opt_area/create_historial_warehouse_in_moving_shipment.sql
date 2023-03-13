-- Table: operational.historial_warehouse_in_moving_shipment

-- DROP TABLE IF EXISTS operational.historial_warehouse_in_moving_shipment;

CREATE TABLE IF NOT EXISTS operational.historial_warehouse_in_moving_shipment
(
    id integer NOT NULL DEFAULT nextval('operational.historial_warehouse_in_moving_shipment_id_seq'::regclass),
    response operational.response,
    reason_of_response text COLLATE pg_catalog."default",
    type operational.type_operation_internal_request NOT NULL,
    code character varying(14) COLLATE pg_catalog."default" NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    destiny_warehouse_id integer NOT NULL,
    origin_warehouse_id integer NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    shipment_id integer NOT NULL,
    CONSTRAINT historial_warehouse_in_moving_shipment_id_idx PRIMARY KEY (id),
    CONSTRAINT historial_warehouse_moving_shipment_code_unique UNIQUE (code),
    CONSTRAINT historial_warehouse_moving_shipment_destiny_warehouse_id FOREIGN KEY (destiny_warehouse_id)
        REFERENCES operational.warehouse (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_warehouse_moving_shipment_origin_warehouse_id FOREIGN KEY (origin_warehouse_id)
        REFERENCES operational.warehouse (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_warehouse_moving_shipment_shipment_id FOREIGN KEY (shipment_id)
        REFERENCES operational.shipment (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_warehouse_moving_shipment_code_format CHECK (code::text ~ '[A-Z]{3}[0-9]{11}$'::text),
    CONSTRAINT historial_warehouse_moving_shipment_not_same_warehouse CHECK (destiny_warehouse_id <> origin_warehouse_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.historial_warehouse_in_moving_shipment
    OWNER to postgres;