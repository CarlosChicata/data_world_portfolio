-- Type: incentive_operation

-- DROP TYPE IF EXISTS operational.incentive_operation;

CREATE TYPE operational.incentive_operation AS ENUM
    ('add', 'multiply');

ALTER TYPE operational.incentive_operation
    OWNER TO postgres;
