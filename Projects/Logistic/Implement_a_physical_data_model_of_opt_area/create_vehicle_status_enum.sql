-- Type: vehicle_status

-- DROP TYPE IF EXISTS operational.vehicle_status;

CREATE TYPE operational.vehicle_status AS ENUM
    ('repaired', 'available', 'unavailable', 'using by driver', 'repairing');

ALTER TYPE operational.vehicle_status
    OWNER TO postgres;
