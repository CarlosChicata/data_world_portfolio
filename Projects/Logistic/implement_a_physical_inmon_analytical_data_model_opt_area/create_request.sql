-- Table: operational.request

-- DROP TABLE IF EXISTS operational.request;

CREATE TABLE IF NOT EXISTS operational.request
(
    id_register integer NOT NULL,
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
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    CONSTRAINT request_id_idx PRIMARY KEY (id_register),
    CONSTRAINT request_branch_id FOREIGN KEY (branch_id)
        REFERENCES operational.branch (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.request
    OWNER to postgres;

-- Index: request_btree_code

-- DROP INDEX IF EXISTS operational.request_btree_code;

CREATE INDEX IF NOT EXISTS request_btree_code
    ON operational.request USING btree
    (id_internal ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.request
    CLUSTER ON request_btree_code;
