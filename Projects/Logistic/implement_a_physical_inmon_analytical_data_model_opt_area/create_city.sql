-- Table: operational.city

-- DROP TABLE IF EXISTS operational.city;

CREATE TABLE IF NOT EXISTS operational.city
(
    id_register integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    time_zone character varying(50) COLLATE pg_catalog."default" NOT NULL,
    area polygon NOT NULL,
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    governal_name character varying(135) COLLATE pg_catalog."default" NOT NULL,
    country_id integer NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT city_id_idx PRIMARY KEY (id_register),
    CONSTRAINT city_country_id FOREIGN KEY (country_id)
        REFERENCES operational.country (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.city
    OWNER to postgres;

-- Index: city_btree_code

-- DROP INDEX IF EXISTS operational.city_btree_code;

CREATE INDEX IF NOT EXISTS city_btree_code
    ON operational.city USING btree
    (id_internal ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.city
    CLUSTER ON city_btree_code;