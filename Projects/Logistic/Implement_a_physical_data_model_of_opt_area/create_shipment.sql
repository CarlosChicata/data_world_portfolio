-- Table: operational.shipment

-- DROP TABLE IF EXISTS operational.shipment;

CREATE TABLE IF NOT EXISTS operational.shipment
(
    code character varying(14) COLLATE pg_catalog."default" NOT NULL,
    use_crossdock boolean NOT NULL DEFAULT false,
    price_product money NOT NULL,
    pickup_address character varying(150) COLLATE pg_catalog."default" NOT NULL,
    pickup_geolocation point NOT NULL,
    pickup_address_reference character varying(100) COLLATE pg_catalog."default" NOT NULL,
    pickup_primary_reference character varying(100) COLLATE pg_catalog."default" NOT NULL,
    pickup_note text COLLATE pg_catalog."default",
    pickup_contact_fullname character varying(100) COLLATE pg_catalog."default" NOT NULL,
    pickup_contact_phone character varying(15) COLLATE pg_catalog."default" NOT NULL,
    pickup_contact_email character varying(30) COLLATE pg_catalog."default",
    pickup_contact_identity_document_value character varying(25) COLLATE pg_catalog."default" NOT NULL,
    pickup_contact_identity_document_type operational.document_identity NOT NULL,
    drop_address character varying(150) COLLATE pg_catalog."default" NOT NULL,
    drop_geolocation point NOT NULL,
    drop_address_reference character varying(100) COLLATE pg_catalog."default" NOT NULL,
    drop_primary_reference character varying(100) COLLATE pg_catalog."default" NOT NULL,
    drop_note text COLLATE pg_catalog."default",
    drop_contact_fullname character varying(100) COLLATE pg_catalog."default" NOT NULL,
    drop_contact_phone character varying(15) COLLATE pg_catalog."default" NOT NULL,
    drop_contact_email character varying(30) COLLATE pg_catalog."default",
    drop_contact_identity_document_value character varying(25) COLLATE pg_catalog."default" NOT NULL,
    drop_contact_identity_document_type operational.document_identity NOT NULL,
    is_damaged boolean NOT NULL DEFAULT false,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    datetime_of_damaged timestamp without time zone NOT NULL DEFAULT now(),
    promise_time timestamp without time zone NOT NULL,
    distance real NOT NULL,
    description_product text COLLATE pg_catalog."default" NOT NULL,
    status operational.shipment_status NOT NULL,
    id integer NOT NULL DEFAULT nextval('operational.shipment_id_seq'::regclass),
    is_delete boolean NOT NULL DEFAULT false,
    warehouse_id integer NOT NULL,
    city_id integer NOT NULL,
    service_id integer NOT NULL,
    branch_id integer NOT NULL,
    city_name character varying(50) COLLATE pg_catalog."default",
    branch_name character varying(80) COLLATE pg_catalog."default",
    warehouse_code character varying(5) COLLATE pg_catalog."default",
    service_name character varying(15) COLLATE pg_catalog."default",
    CONSTRAINT shipment_id_idx PRIMARY KEY (id),
    CONSTRAINT shipment_code_unique UNIQUE (code),
    CONSTRAINT shipment_branch_id FOREIGN KEY (branch_id)
        REFERENCES operational.branch (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT shipment_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT shipment_service_id FOREIGN KEY (service_id)
        REFERENCES operational.service (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT shipment_warehouse_id FOREIGN KEY (warehouse_id)
        REFERENCES operational.warehouse (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT shipment_code_format CHECK (code::text ~ '[A-Z]{3}[0-9]{11}$'::text)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.shipment
    OWNER to postgres;