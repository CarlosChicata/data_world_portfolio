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
    id_register integer NOT NULL,
    id_internal serial NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    route_id integer NOT NULL,
    shipment_id integer NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    drop_geolocation_id integer NOT NULL,
    pickup_geolocation_id integer NOT NULL,
    code_route character varying(14) COLLATE pg_catalog."default",
    transfered_order_id integer,
    CONSTRAINT order_id_idx PRIMARY KEY (id_register),
    CONSTRAINT order_last_incident_id FOREIGN KEY (transfered_order_id)
        REFERENCES operational."order" (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT order_route_id FOREIGN KEY (route_id)
        REFERENCES operational.route (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT order_shipment_id FOREIGN KEY (shipment_id)
        REFERENCES operational.shipment (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT order_drop_loc_id FOREIGN KEY (drop_geolocation_id)
        REFERENCES operational.location (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT order_pickup_loc_id FOREIGN KEY (pickup_geolocation_id)
        REFERENCES operational.location (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational."order"
    OWNER to postgres;

-- Index: order_btreae_code

-- DROP INDEX IF EXISTS operational.order_btreae_code;

CREATE INDEX IF NOT EXISTS order_btree_code
    ON operational."order" USING btree
    (id_internal ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational."order"
    CLUSTER ON order_btree_code;