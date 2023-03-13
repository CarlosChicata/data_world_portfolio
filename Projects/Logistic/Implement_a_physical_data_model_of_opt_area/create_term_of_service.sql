-- Table: operational.term_of_service

-- DROP TABLE IF EXISTS operational.term_of_service;

CREATE TABLE IF NOT EXISTS operational.term_of_service
(
    id integer NOT NULL DEFAULT nextval('operational.term_of_service_id_seq'::regclass),
    is_delete boolean NOT NULL DEFAULT false,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    compensation_term_id integer NOT NULL,
    service_id integer NOT NULL,
    CONSTRAINT term_of_service_id_idx PRIMARY KEY (id),
    CONSTRAINT term_of_service_service_id FOREIGN KEY (service_id)
        REFERENCES operational.service (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT term_of_service_term_id FOREIGN KEY (compensation_term_id)
        REFERENCES operational.compensation_incomplete_term (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.term_of_service
    OWNER to postgres;