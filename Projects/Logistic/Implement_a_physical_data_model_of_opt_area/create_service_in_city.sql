-- Table: operational.service_in_city

-- DROP TABLE IF EXISTS operational.service_in_city;

CREATE TABLE IF NOT EXISTS operational.service_in_city
(
    id integer NOT NULL DEFAULT nextval('operational.service_in_city_id_seq'::regclass),
    service_id integer NOT NULL,
    city_id integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT service_in_city_id_idx PRIMARY KEY (id),
    CONSTRAINT service_in_city_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT service_in_city_service_id FOREIGN KEY (service_id)
        REFERENCES operational.service (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.service_in_city
    OWNER to postgres;