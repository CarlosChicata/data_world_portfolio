-- Type: score_role

-- DROP TYPE IF EXISTS operational.score_role;

CREATE TYPE operational.score_role AS ENUM
    ('inside area', 'cross area', 'regional area', 'cross regional area');

ALTER TYPE operational.score_role
    OWNER TO postgres;