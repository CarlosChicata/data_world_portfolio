-- Type: incident_responsibility

-- DROP TYPE IF EXISTS operational.incident_responsibility;

CREATE TYPE operational.incident_responsibility AS ENUM
    ('mandalo_ours', 'end_client', 'external_event', 'others', 'client');

ALTER TYPE operational.incident_responsibility
    OWNER TO postgres;
