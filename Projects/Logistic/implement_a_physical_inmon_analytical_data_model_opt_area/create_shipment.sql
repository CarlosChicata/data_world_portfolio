-- Table: operational.shipment

-- DROP TABLE IF EXISTS operational.shipment;

CREATE TABLE IF NOT EXISTS operational.shipment
(
    code character varying(14) COLLATE pg_catalog."default" NOT NULL,
    use_crossdock boolean NOT NULL DEFAULT false,
    price_product money NOT NULL
    pickup_location integer NOT NULL,
    drop_location integer NOT NULL,
    is_damaged boolean NOT NULL DEFAULT false,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    datetime_of_damaged timestamp without time zone NOT NULL DEFAULT now(),
    promise_time timestamp without time zone NOT NULL,
    distance real NOT NULL,
    description_product text COLLATE pg_catalog."default" NOT NULL,
    status operational.shipment_status NOT NULL,
    id_register integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    warehouse_id integer NOT NULL,
    city_id integer NOT NULL,
    id_internal serial NOT NULL,
    service_id integer NOT NULL,
    branch_id integer NOT NULL,
    service_name character varying(15) COLLATE pg_catalog."default",
    CONSTRAINT shipment_id_idx PRIMARY KEY (id_register),
    CONSTRAINT shipment_branch_id FOREIGN KEY (branch_id)
        REFERENCES operational.branch (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT shipment_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT shipment_service_id FOREIGN KEY (service_id)
        REFERENCES operational.service (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT shipment_warehouse_id FOREIGN KEY (warehouse_id)
        REFERENCES operational.warehouse (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.shipment
    OWNER to postgres;

-- Index: shipment_btree_code

-- DROP INDEX IF EXISTS operational.shipment_btree_code;

CREATE INDEX IF NOT EXISTS shipment_btree_code
    ON operational.shipment USING btree
    (id_internal ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.shipment
    CLUSTER ON shipment_btree_code;