-- Table: operational.historial_warehouse_in_moving_vehicle

-- DROP TABLE IF EXISTS operational.historial_warehouse_in_moving_vehicle;

CREATE TABLE IF NOT EXISTS operational.historial_warehouse_in_moving_vehicle
(
    id integer NOT NULL DEFAULT nextval('operational.historial_warehouse_in_moving_vehicle_id_seq'::regclass),
    creation timestamp without time zone NOT NULL DEFAULT now(),
    response operational.response,
    reason_of_response text COLLATE pg_catalog."default",
    type operational.type_operation_internal_request NOT NULL,
    code character varying(14) COLLATE pg_catalog."default" NOT NULL,
    vehicle_id integer NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    destiny_warehouse_id integer NOT NULL,
    origin_warehouse_id integer NOT NULL,
    CONSTRAINT historial_warehouse_moving_vehicle_id_idx PRIMARY KEY (id),
    CONSTRAINT historial_warehouse_moving_vehicle_code_unique UNIQUE (code),
    CONSTRAINT historial_warehouse_moving_vehicle_destiny_warehouse_id FOREIGN KEY (destiny_warehouse_id)
        REFERENCES operational.warehouse (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_warehouse_moving_vehicle_origin_vehicle_id FOREIGN KEY (origin_warehouse_id)
        REFERENCES operational.warehouse (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_warehouse_moving_vehicle_vehicle_id FOREIGN KEY (vehicle_id)
        REFERENCES operational.vehicle (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_warehouse_moving_vehicle_code_format CHECK (code::text ~ '[A-Z]{3}[0-9]{11}$'::text),
    CONSTRAINT historial_warehouse_moving_vehicle_not_same_warehouse CHECK (destiny_warehouse_id <> origin_warehouse_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.historial_warehouse_in_moving_vehicle
    OWNER to postgres;