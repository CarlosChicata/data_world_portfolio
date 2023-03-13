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
    id serial NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    CONSTRAINT country_idx_id PRIMARY KEY (id),
    CONSTRAINT country_gov_name_unique UNIQUE (governal_name),
    CONSTRAINT country_name_unique UNIQUE (name),
    CONSTRAINT country_prefix_phone_format CHECK (prefix_phone::text ~* '\+[0-9\ ]{0,11}'::text)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.country
    OWNER to postgres;
