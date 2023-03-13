-- Table: operational.user

-- DROP TABLE IF EXISTS operational."user";

CREATE TABLE IF NOT EXISTS operational."user"
(
    first_name character varying(80) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(80) COLLATE pg_catalog."default" NOT NULL,
    birthday date NOT NULL,
    document_identity_type operational.document_identity NOT NULL,
    document_identity_value character varying(25) COLLATE pg_catalog."default" NOT NULL,
    is_validated boolean NOT NULL DEFAULT false,
    validated timestamp without time zone,
    bank_number_account character varying(15) COLLATE pg_catalog."default" NOT NULL,
    has_legal_background_documents boolean,
    id integer NOT NULL DEFAULT nextval('operational.user_id_seq'::regclass),
    is_delete boolean NOT NULL DEFAULT false,
    city_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    city_id integer NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT user_id_idx PRIMARY KEY (id),
    CONSTRAINT user_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational."user"
    OWNER to postgres;