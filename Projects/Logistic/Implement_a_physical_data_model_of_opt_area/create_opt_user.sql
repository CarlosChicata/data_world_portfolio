-- Table: operational.operational_user

-- DROP TABLE IF EXISTS operational.operational_user;

CREATE TABLE IF NOT EXISTS operational.operational_user
(
    period_of_pay int4range NOT NULL,
    id integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    main_role integer NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT opt_user_id_idx PRIMARY KEY (id),
    CONSTRAINT opt_user_role_id FOREIGN KEY (main_role)
        REFERENCES operational.role (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT opt_user_user_id FOREIGN KEY (id)
        REFERENCES operational."user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.operational_user
    OWNER to postgres;