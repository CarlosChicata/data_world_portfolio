-- Table: operational.term_of_request

-- DROP TABLE IF EXISTS operational.term_of_request;

CREATE TABLE IF NOT EXISTS operational.term_of_request
(
    id integer NOT NULL DEFAULT nextval('operational.term_of_request_id_seq'::regclass),
    is_delete boolean NOT NULL DEFAULT false,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    request_id integer NOT NULL,
    compensation_term_id integer NOT NULL,
    CONSTRAINT term_of_request_id_idx PRIMARY KEY (id),
    CONSTRAINT term_of_request_request_id FOREIGN KEY (request_id)
        REFERENCES operational.request (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT term_of_request_term_id FOREIGN KEY (compensation_term_id)
        REFERENCES operational.compensation_incomplete_term (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.term_of_request
    OWNER to postgres;