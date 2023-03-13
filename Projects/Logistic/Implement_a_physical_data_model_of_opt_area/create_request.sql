-- Table: operational.request

-- DROP TABLE IF EXISTS operational.request;

CREATE TABLE IF NOT EXISTS operational.request
(
    id integer NOT NULL DEFAULT nextval('operational.request_id_seq'::regclass),
    code character varying COLLATE pg_catalog."default" NOT NULL,
    price money,
    description text COLLATE pg_catalog."default" NOT NULL,
    response operational.response,
    reason_response character varying(120) COLLATE pg_catalog."default",
    resource_type operational.resource_type NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    response_datetime timestamp without time zone,
    start_datetime timestamp without time zone NOT NULL,
    finsh_datetime timestamp without time zone NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    branch_id integer NOT NULL,
    CONSTRAINT request_id_idx PRIMARY KEY (id),
    CONSTRAINT request_code_unique UNIQUE (code),
    CONSTRAINT request_branch_id FOREIGN KEY (branch_id)
        REFERENCES operational.branch (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT request_code_format CHECK (code::text ~ '[A-Z]{3}[0-9]{11}$'::text)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.request
    OWNER to postgres;