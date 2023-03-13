-- Table: operational.status_event_order

-- DROP TABLE IF EXISTS operational.status_event_order;

CREATE TABLE IF NOT EXISTS operational.status_event_order
(
    id_register integer NOT NULL,
    status operational.shipment_status NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    order_id integer NOT NULL,
    is_delete boolean NOT NULL,
    incident_id integer,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    id_internal serial NOT NULL,
    CONSTRAINT status_event_order_id_idx PRIMARY KEY (id_register),
    CONSTRAINT status_event_order_incident_id FOREIGN KEY (incident_id)
        REFERENCES operational.incident (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT status_event_order_order_id FOREIGN KEY (order_id)
        REFERENCES operational."order" (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.status_event_order
    OWNER to postgres;