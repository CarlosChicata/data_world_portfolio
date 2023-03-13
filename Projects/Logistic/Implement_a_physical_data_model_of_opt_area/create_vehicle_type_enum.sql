-- Type: vehicle_type

-- DROP TYPE IF EXISTS operational.vehicle_type;

CREATE TYPE operational.vehicle_type AS ENUM
    ('moto', 'van', 'convoy', 'car');

ALTER TYPE operational.vehicle_type
    OWNER TO postgres;