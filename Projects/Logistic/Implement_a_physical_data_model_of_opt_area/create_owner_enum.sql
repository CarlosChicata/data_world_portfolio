-- Type: owner

-- DROP TYPE IF EXISTS operational.owner;

CREATE TYPE operational.owner AS ENUM
    ('driver', 'ours');

ALTER TYPE operational.owner
    OWNER TO postgres;
