-- Table: operational.status_event_order

-- DROP TABLE IF EXISTS operational.status_event_order;

CREATE TABLE IF NOT EXISTS operational.status_event_order
(
    id integer NOT NULL DEFAULT nextval('operational.status_event_order_id_seq'::regclass),
    status operational.shipment_status NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    order_id integer NOT NULL,
    is_delete boolean NOT NULL,
    incident_id integer,
    incident_name character varying(50) COLLATE pg_catalog."default",
    incident_responsibility character varying(12) COLLATE pg_catalog."default",
    created_user_type operational.created_user_type NOT NULL,
    CONSTRAINT status_event_order_id_idx PRIMARY KEY (id),
    CONSTRAINT status_event_order_incident_id FOREIGN KEY (incident_id)
        REFERENCES operational.incident (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT status_event_order_order_id FOREIGN KEY (order_id)
        REFERENCES operational."order" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.status_event_order
    OWNER to postgres;