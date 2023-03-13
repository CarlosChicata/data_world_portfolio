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
    id_register integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    vehicle_id integer NOT NULL,
    driver_id integer NOT NULL,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    liquidation_datetime timestamp without time zone,
    CONSTRAINT route_id_idx PRIMARY KEY (id_register),
    CONSTRAINT route_driver_id FOREIGN KEY (driver_id)
        REFERENCES operational.driver (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT route_vehicle_id FOREIGN KEY (vehicle_id)
        REFERENCES operational.vehicle (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.route
    OWNER to postgres;

-- Index: route_btree_code

-- DROP INDEX IF EXISTS operational.route_btree_code;

CREATE INDEX IF NOT EXISTS route_btree_code
    ON operational.route USING btree
    (id_internal ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.route
    CLUSTER ON route_btree_code;