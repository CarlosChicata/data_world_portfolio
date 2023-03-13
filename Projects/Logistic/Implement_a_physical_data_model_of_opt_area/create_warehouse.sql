-- Table: operational.warehouse

-- DROP TABLE IF EXISTS operational.warehouse;

CREATE TABLE IF NOT EXISTS operational.warehouse
(
    id integer NOT NULL DEFAULT nextval('operational.warehouse_id_seq'::regclass),
    address character varying(120) COLLATE pg_catalog."default" NOT NULL,
    address_geolocation point NOT NULL,
    phone character varying(20) COLLATE pg_catalog."default" NOT NULL,
    area polygon NOT NULL,
    can_receive_vehicle_from_other_city boolean NOT NULL DEFAULT true,
    max_capacity_of_received_vehicle json NOT NULL,
    max_capacity_of_shipment json NOT NULL,
    code character varying(5) COLLATE pg_catalog."default" NOT NULL,
    current_vehicle_internal_store json NOT NULL,
    city_id integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT warehouse_id_idx PRIMARY KEY (id),
    CONSTRAINT warehouse_code_unique UNIQUE (code),
    CONSTRAINT warehouse_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT warehouse_code_format CHECK (code::text ~ '[A-Z]{3}[0-9]{2}$'::text)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.warehouse
    OWNER to postgres;