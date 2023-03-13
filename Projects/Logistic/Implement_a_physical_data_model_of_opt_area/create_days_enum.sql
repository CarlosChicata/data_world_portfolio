-- Type: days

-- DROP TYPE IF EXISTS operational.days;

CREATE TYPE operational.days AS ENUM
    ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo');

ALTER TYPE operational.days
    OWNER TO postgres;