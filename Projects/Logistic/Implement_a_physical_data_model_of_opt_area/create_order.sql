-- Table: operational.order

-- DROP TABLE IF EXISTS operational."order";

CREATE TABLE IF NOT EXISTS operational."order"
(
    start_datetime timestamp without time zone,
    finish_datetime timestamp without time zone,
    price money,
    is_transfered boolean NOT NULL DEFAULT false,
    reason_of_transfered text COLLATE pg_catalog."default",
    datetime_of_transfered timestamp without time zone,
    is_remove boolean NOT NULL DEFAULT false,
    reason_of_remove text COLLATE pg_catalog."default",
    status operational.shipment_status NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    id integer NOT NULL DEFAULT nextval('operational.order_id_seq'::regclass),
    is_delete boolean NOT NULL DEFAULT false,
    route_id integer NOT NULL,
    shipment_id integer NOT NULL,
    last_incident_id integer,
    drop_geolocation point NOT NULL,
    pickup_geolocation point NOT NULL,
    code_shipment character varying(14) COLLATE pg_catalog."default",
    code_route character varying(14) COLLATE pg_catalog."default",
    transfered_order_id integer,
    CONSTRAINT order_id_idx PRIMARY KEY (id),
    CONSTRAINT order_last_incident_id FOREIGN KEY (last_incident_id)
        REFERENCES operational.incident (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT order_route_id FOREIGN KEY (route_id)
        REFERENCES operational.route (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT order_shipment_id FOREIGN KEY (shipment_id)
        REFERENCES operational.shipment (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational."order"
    OWNER to postgres;