-- Type: route_type

-- DROP TYPE IF EXISTS operational.route_type;

CREATE TYPE operational.route_type AS ENUM
    ('offered', 'assigned');

ALTER TYPE operational.route_type
    OWNER TO postgres;
