-- Table: operational.role

-- DROP TABLE IF EXISTS operational.role;

CREATE TABLE IF NOT EXISTS operational.role
(
    id integer NOT NULL DEFAULT nextval('operational.role_id_seq'::regclass),
    title character varying COLLATE pg_catalog."default" NOT NULL,
    description character varying(150) COLLATE pg_catalog."default" NOT NULL,
    responsibility text COLLATE pg_catalog."default",
    score operational.score_role NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    CONSTRAINT role_id_idx PRIMARY KEY (id),
    CONSTRAINT role_title_unique UNIQUE (title)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.role
    OWNER to postgres;