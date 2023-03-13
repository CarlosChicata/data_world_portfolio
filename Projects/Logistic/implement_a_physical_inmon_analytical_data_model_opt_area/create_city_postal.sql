-- Table: operational.city_postal

-- DROP TABLE IF EXISTS operational.city_postal;

CREATE TABLE IF NOT EXISTS operational.city_postal
(
    zip_post character varying(10) COLLATE pg_catalog."default" NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    city_id integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    CONSTRAINT country_idx_id PRIMARY KEY (id_internal),
    CONSTRAINT city_postal_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.city_postal
    OWNER to postgres;
