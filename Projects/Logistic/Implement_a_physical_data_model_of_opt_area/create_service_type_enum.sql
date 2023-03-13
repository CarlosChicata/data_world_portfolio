-- Type: service_type

-- DROP TYPE IF EXISTS operational.service_type;

CREATE TYPE operational.service_type AS ENUM
    ('resource based', 'order based');

ALTER TYPE operational.service_type
    OWNER TO postgres;
