-- Table: operational.resource_of_request

-- DROP TABLE IF EXISTS operational.resource_of_request;

CREATE TABLE IF NOT EXISTS operational.resource_of_request
(
    id integer NOT NULL DEFAULT nextval('operational.resource_of_request_id_seq'::regclass),
    is_delete boolean NOT NULL DEFAULT false,
    type operational.resource_type NOT NULL,
    request_id integer NOT NULL,
    code_request character varying(14) COLLATE pg_catalog."default" NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    resource_id integer NOT NULL,
    CONSTRAINT resource_of_request_id_idx PRIMARY KEY (id),
    CONSTRAINT resource_of_request_request_id FOREIGN KEY (request_id)
        REFERENCES operational.request (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.resource_of_request
    OWNER to postgres;
-- Index: fki_-- Table: operational.resource_of_request  -- DROP TABLE IF

-- DROP INDEX IF EXISTS operational."fki_-- Table: operational.resource_of_request  -- DROP TABLE IF";

CREATE INDEX IF NOT EXISTS "fki_-- Table: operational.resource_of_request  -- DROP TABLE IF"
    ON operational.resource_of_request USING btree
    (request_id ASC NULLS LAST)
    TABLESPACE pg_default;