-- Type: document_identity

-- DROP TYPE IF EXISTS operational.document_identity;

CREATE TYPE operational.document_identity AS ENUM
    ('DNI', 'Pasaporte', 'Cedula de identidad');

ALTER TYPE operational.document_identity
    OWNER TO postgres;