-- Table: operational.historial_warehouse_in_moving_resource

-- DROP TABLE IF EXISTS operational.historial_warehouse_in_moving_resource;

CREATE TABLE IF NOT EXISTS operational.historial_warehouse_in_moving_resource
(
    id_register integer NOT NULL,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    response operational.response,
    reason_of_response text COLLATE pg_catalog."default",
    type operational.type_operation_internal_request NOT NULL,
    code character varying(14) COLLATE pg_catalog."default" NOT NULL,
    destiny_warehouse_id integer NOT NULL,
    origin_warehouse_id integer NOT NULL,
    CONSTRAINT historial_warehouse_moving_vehicle_id_idx PRIMARY KEY (id_register),
    CONSTRAINT historial_warehouse_moving_vehicle_destiny_warehouse_id FOREIGN KEY (destiny_warehouse_id)
        REFERENCES operational.warehouse (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT historial_warehouse_moving_vehicle_origin_vehicle_id FOREIGN KEY (origin_warehouse_id)
        REFERENCES operational.warehouse (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.historial_warehouse_in_moving_resource
    OWNER to postgres;
