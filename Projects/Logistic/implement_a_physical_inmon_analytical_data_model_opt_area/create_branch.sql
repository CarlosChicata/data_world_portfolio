-- Table: operational.branch

-- DROP TABLE IF EXISTS operational.branch;

CREATE TABLE IF NOT EXISTS operational.branch
(
    commercial_name character varying(80) COLLATE pg_catalog."default" NOT NULL,
    business_name character varying(40) COLLATE pg_catalog."default" NOT NULL,
    code character varying(3) COLLATE pg_catalog."default" NOT NULL,
    address character varying(120) COLLATE pg_catalog."default" NOT NULL,
    address_geolocation point NOT NULL,
    legal_representative_fullname character varying(120) COLLATE pg_catalog."default" NOT NULL,
    id_register integer NOT NULL,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    city_id integer NOT NULL,
    enterprise_id integer NOT NULL,
    CONSTRAINT branch_id_idx PRIMARY KEY (id_register),
    CONSTRAINT branch_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT branch_enterprise_id FOREIGN KEY (enterprise_id)
        REFERENCES operational.enterprise (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.branch
    OWNER to postgres;

-- Index: branch_btree_code

-- DROP INDEX IF EXISTS operational.branch_btree_code;

CREATE INDEX IF NOT EXISTS branch_btree_code
    ON operational.branch USING btree
    (id_internal ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.branch
    CLUSTER ON branch_btree_code;