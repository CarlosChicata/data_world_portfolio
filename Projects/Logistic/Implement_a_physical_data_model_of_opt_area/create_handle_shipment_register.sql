-- Table: operational.handle_shipment_register

-- DROP TABLE IF EXISTS operational.handle_shipment_register;

CREATE TABLE IF NOT EXISTS operational.handle_shipment_register
(
    id integer NOT NULL DEFAULT nextval('operational.handle_shipment_register_id_seq'::regclass),
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    status_changed_shipment operational.shipment_status NOT NULL,
    status_previos_shipment operational.shipment_status NOT NULL,
    shipment_id integer NOT NULL,
    list_changes operational.change_shipment[] NOT NULL,
    CONSTRAINT handle_shipment_register_id_idx PRIMARY KEY (id),
    CONSTRAINT handle_shipment_register_shipment_id FOREIGN KEY (shipment_id)
        REFERENCES operational.shipment (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.handle_shipment_register
    OWNER to postgres;