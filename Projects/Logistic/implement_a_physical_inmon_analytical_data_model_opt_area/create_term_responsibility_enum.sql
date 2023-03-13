-- Type: term_responsibility

-- DROP TYPE IF EXISTS operational.term_responsibility;

CREATE TYPE operational.term_responsibility AS ENUM
    ('client', 'ours');

ALTER TYPE operational.term_responsibility
    OWNER TO postgres;
