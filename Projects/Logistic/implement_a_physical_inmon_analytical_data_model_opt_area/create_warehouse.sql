-- Table: operational.warehouse

-- DROP TABLE IF EXISTS operational.warehouse;

CREATE TABLE IF NOT EXISTS operational.warehouse
(
    id_register integer NOT NULL,
    address character varying(120) COLLATE pg_catalog."default" NOT NULL,
    address_geolocation point NOT NULL,
    area polygon NOT NULL,
    can_receive_vehicle_from_other_city boolean NOT NULL DEFAULT true,
    city_id integer NOT NULL,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    CONSTRAINT warehouse_id_idx PRIMARY KEY (id_register),
    CONSTRAINT warehouse_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.warehouse
    OWNER to postgres;