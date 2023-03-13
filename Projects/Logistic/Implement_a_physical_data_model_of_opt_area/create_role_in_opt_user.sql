-- Table: operational.role_in_optuser

-- DROP TABLE IF EXISTS operational.role_in_optuser;

CREATE TABLE IF NOT EXISTS operational.role_in_optuser
(
    start_apply timestamp without time zone NOT NULL DEFAULT now(),
    finish_apply timestamp without time zone NOT NULL,
    id integer NOT NULL DEFAULT nextval('operational.role_in_optuser_id_seq'::regclass),
    is_delete boolean NOT NULL,
    role_id integer NOT NULL,
    optuser_id integer NOT NULL,
    creation timestamp without time zone DEFAULT now(),
    CONSTRAINT role_opt_user_id PRIMARY KEY (id),
    CONSTRAINT role_optuser_optuser_id FOREIGN KEY (optuser_id)
        REFERENCES operational.operational_user (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT role_optuser_role_id FOREIGN KEY (role_id)
        REFERENCES operational.role (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.role_in_optuser
    OWNER to postgres;