-- Type: type_operation_internal_request

-- DROP TYPE IF EXISTS operational.type_operation_internal_request;

CREATE TYPE operational.type_operation_internal_request AS ENUM
    ('get in', 'get out');

ALTER TYPE operational.type_operation_internal_request
    OWNER TO postgres;
