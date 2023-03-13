-- Table: operational.city

-- DROP TABLE IF EXISTS operational.city;

CREATE TABLE IF NOT EXISTS operational.city
(
    id integer NOT NULL DEFAULT nextval('operational.city_id_seq'::regclass),
    time_zone character varying(50) COLLATE pg_catalog."default" NOT NULL,
    area polygon NOT NULL,
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    governal_name character varying(135) COLLATE pg_catalog."default" NOT NULL,
    zip_codes character varying[] COLLATE pg_catalog."default",
    is_delete boolean NOT NULL DEFAULT false,
    country_id integer NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT city_id_idx PRIMARY KEY (id),
    CONSTRAINT city_gov_name_unique UNIQUE (governal_name),
    CONSTRAINT city_country_id FOREIGN KEY (country_id)
        REFERENCES operational.country (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.city
    OWNER to postgres;