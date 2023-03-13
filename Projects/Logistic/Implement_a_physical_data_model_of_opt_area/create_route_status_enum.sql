-- Type: route_status

-- DROP TYPE IF EXISTS operational.route_status;

CREATE TYPE operational.route_status AS ENUM
    ('created', 'dispatched', 'completed', 'working', 'cancelled', 'transfered', 'accepted', 'offered');

ALTER TYPE operational.route_status
    OWNER TO postgres;
