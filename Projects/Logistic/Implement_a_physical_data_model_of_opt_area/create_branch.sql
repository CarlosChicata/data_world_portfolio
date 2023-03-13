-- Table: operational.branch

-- DROP TABLE IF EXISTS operational.branch;

CREATE TABLE IF NOT EXISTS operational.branch
(
    commercial_name character varying(80) COLLATE pg_catalog."default" NOT NULL,
    business_name character varying(40) COLLATE pg_catalog."default" NOT NULL,
    corporative_phone character varying(20) COLLATE pg_catalog."default" NOT NULL,
    corporative_email character varying(50) COLLATE pg_catalog."default" NOT NULL,
    code character varying(3) COLLATE pg_catalog."default" NOT NULL,
    address character varying(120) COLLATE pg_catalog."default" NOT NULL,
    address_geolocation point NOT NULL,
    legal_representative_fullname character varying(120) COLLATE pg_catalog."default" NOT NULL,
    id serial NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    city_id integer NOT NULL,
    schedules operational.branch_schedule[],
    enterprise_id integer NOT NULL,
    CONSTRAINT branch_id_idx PRIMARY KEY (id),
    CONSTRAINT branch_biz_name_unique UNIQUE (business_name),
    CONSTRAINT branch_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT branch_enterprise_id FOREIGN KEY (enterprise_id)
        REFERENCES operational.enterprise (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT branch_check_phone CHECK (corporative_phone::text ~* '\+[0-9\ ]{6,18}'::text)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.branch
    OWNER to postgres;