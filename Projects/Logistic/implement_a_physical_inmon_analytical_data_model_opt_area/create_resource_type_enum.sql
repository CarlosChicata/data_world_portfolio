-- Type: resource_type

-- DROP TYPE IF EXISTS operational.resource_type;

CREATE TYPE operational.resource_type AS ENUM
    ('driver', 'warehouse', 'vehicle');

ALTER TYPE operational.resource_type
    OWNER TO postgres;
