-- Type: response

-- DROP TYPE IF EXISTS operational.response;

CREATE TYPE operational.response AS ENUM
    ('accepted', 'rejected');

ALTER TYPE operational.response
    OWNER TO postgres;