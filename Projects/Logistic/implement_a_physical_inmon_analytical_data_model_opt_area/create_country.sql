-- Table: operational.country

-- DROP TABLE IF EXISTS operational.country;

CREATE TABLE IF NOT EXISTS operational.country
(
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    governal_name character varying(120) COLLATE pg_catalog."default" NOT NULL,
    prefix_phone character varying(12) COLLATE pg_catalog."default" NOT NULL,
    currency_iso character varying(5) COLLATE pg_catalog."default" NOT NULL,
    acronomy character varying(5) COLLATE pg_catalog."default",
    area polygon NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    id_register integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    CONSTRAINT country_idx_id PRIMARY KEY (id_register),
    CONSTRAINT country_prefix_phone_format CHECK (prefix_phone::text ~* '\+[0-9\ ]{0,11}'::text)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.country
    OWNER to postgres;

-- Index: country_btree_code

-- DROP INDEX IF EXISTS operational.country_btree_code;

CREATE INDEX IF NOT EXISTS country_btree_code
    ON operational.country USING btree
    (id_internal ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.city
    CLUSTER ON country_btree_code;