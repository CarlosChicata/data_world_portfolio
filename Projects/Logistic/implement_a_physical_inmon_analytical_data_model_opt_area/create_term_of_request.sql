-- Table: operational.term_of_request

-- DROP TABLE IF EXISTS operational.term_of_request;

CREATE TABLE IF NOT EXISTS operational.term_of_request
(
    id_register integer NOT NULL,
    request_id integer NOT NULL,
    term_id integer NOT NULL,
    CONSTRAINT term_of_request_id_idx PRIMARY KEY (id_register),
    CONSTRAINT term_of_request_term_id FOREIGN KEY (term_id)
        REFERENCES operational.compensation_incomplete_term (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT term_of_request_request_id FOREIGN KEY (request_id)
        REFERENCES operational.request (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.term_of_request
    OWNER to postgres;
