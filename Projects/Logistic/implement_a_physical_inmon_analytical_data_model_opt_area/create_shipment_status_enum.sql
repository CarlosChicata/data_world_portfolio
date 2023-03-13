-- Type: shipment_status

-- DROP TYPE IF EXISTS operational.shipment_status;

CREATE TYPE operational.shipment_status AS ENUM
    ('cancelled', 'validated', 'start', 'picked_up', 'picking_up', 'delivering', 'failed_pickup', 'failed_delivery', 'returning', 'crossdocking', 'finished', 'crossdocked', 'delivered');

ALTER TYPE operational.shipment_status
    OWNER TO postgres;