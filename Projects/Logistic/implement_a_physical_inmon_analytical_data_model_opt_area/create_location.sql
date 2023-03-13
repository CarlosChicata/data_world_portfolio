-- Table: operational.location

-- DROP TABLE IF EXISTS operational.location;

CREATE TABLE IF NOT EXISTS operational.location
(
    address character varying(150) COLLATE pg_catalog."default" NOT NULL,
    geolocation point NOT NULL,
    address_reference character varying(100) COLLATE pg_catalog."default" NOT NULL,
    primary_reference character varying(100) COLLATE pg_catalog."default" NOT NULL,
    note text COLLATE pg_catalog."default",
    contact_fullname character varying(100) COLLATE pg_catalog."default" NOT NULL,
    contact_phone character varying(15) COLLATE pg_catalog."default" NOT NULL,
    contact_email character varying(30) COLLATE pg_catalog."default",
    contact_identity_document_value character varying(25) COLLATE pg_catalog."default" NOT NULL,
    contact_identity_document_type operational.document_identity NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    id_register integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    CONSTRAINT country_idx_id PRIMARY KEY (id_register),
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.location
    OWNER to postgres;
