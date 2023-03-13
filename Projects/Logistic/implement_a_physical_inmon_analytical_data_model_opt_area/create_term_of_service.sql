-- Table: operational.term_of_service

-- DROP TABLE IF EXISTS operational.term_of_service;

CREATE TABLE IF NOT EXISTS operational.term_of_service
(
    id_register integer NOT NULL,
    service_id integer NOT NULL,
    term_id integer NOT NULL,
    CONSTRAINT term_of_request_id_idx PRIMARY KEY (id_register),
    CONSTRAINT term_of_request_term_id FOREIGN KEY (term_id)
        REFERENCES operational.compensation_incomplete_term (id_register) MATCH S
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT term_of_request_service_id FOREIGN KEY (service_id)
        REFERENCES operational.service (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.term_of_service
    OWNER to postgres;
