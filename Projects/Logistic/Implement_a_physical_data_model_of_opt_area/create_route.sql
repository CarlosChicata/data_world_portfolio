-- Table: operational.route

-- DROP TABLE IF EXISTS operational.route;

CREATE TABLE IF NOT EXISTS operational.route
(
    start_datetime timestamp without time zone,
    finish_datetime timestamp without time zone,
    price money,
    incentive_operational operational.incentive_operation,
    incentive_price real,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    type operational.route_type NOT NULL,
    is_liquidation boolean NOT NULL DEFAULT false,
    code character varying(14) COLLATE pg_catalog."default" NOT NULL,
    status operational.route_status NOT NULL,
    id integer NOT NULL DEFAULT nextval('operational.route_id_seq'::regclass),
    is_delete boolean NOT NULL DEFAULT false,
    vehicle_id integer NOT NULL,
    driver_id integer NOT NULL,
    liquidation_datetime timestamp without time zone,
    CONSTRAINT route_id_idx PRIMARY KEY (id),
    CONSTRAINT route_code_unique UNIQUE (code),
    CONSTRAINT route_driver_id FOREIGN KEY (driver_id)
        REFERENCES operational.driver (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT route_vehicle_id FOREIGN KEY (vehicle_id)
        REFERENCES operational.vehicle (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT route_consistence_incentive CHECK (
CASE
    WHEN incentive_operational IS NOT NULL AND incentive_price IS NULL THEN false
    WHEN incentive_operational IS NULL AND incentive_price IS NOT NULL THEN false
    ELSE true
END)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.route
    OWNER to postgres;