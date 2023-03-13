-- Type: operation_change_shipment

-- DROP TYPE IF EXISTS operational.operation_change_shipment;

CREATE TYPE operational.operation_change_shipment AS ENUM
    ('delete', 'create', 'update');

ALTER TYPE operational.operation_change_shipment
    OWNER TO postgres;