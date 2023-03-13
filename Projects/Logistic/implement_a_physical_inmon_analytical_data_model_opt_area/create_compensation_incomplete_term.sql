-- Table: operational.compensation_incomplete_term

-- DROP TABLE IF EXISTS operational.compensation_incomplete_term;

CREATE TABLE IF NOT EXISTS operational.compensation_incomplete_term
(
    id_register integer NOT NULL,
    title character varying(80) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    responsibility operational.term_responsibility NOT NULL,
    price money NOT NULL DEFAULT 0.00,
    is_delete boolean NOT NULL DEFAULT false,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT compensation_incomplete_term_id_idx PRIMARY KEY (id_register)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.compensation_incomplete_term
    OWNER to postgres;