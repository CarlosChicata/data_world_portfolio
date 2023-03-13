-- Type: created_user_type

-- DROP TYPE IF EXISTS operational.created_user_type;

CREATE TYPE operational.created_user_type AS ENUM
    ('driver', 'operational_user');

ALTER TYPE operational.created_user_type
    OWNER TO postgres;