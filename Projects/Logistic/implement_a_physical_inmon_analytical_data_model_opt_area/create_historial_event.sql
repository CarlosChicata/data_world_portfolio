-- Table: operational.historial_event

-- DROP TABLE IF EXISTS operational.historial_event;

CREATE TABLE IF NOT EXISTS operational.historial_event
(
    id_register integer NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    start_apply timestamp without time zone NOT NULL,
    finish_apply timestamp without time zone NOT NULL,
    response operational.response,
    reason_of_reponse text COLLATE pg_catalog."default",
    is_delete boolean NOT NULL DEFAULT false,
    datetime_response timestamp without time zone,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    CONSTRAINT historial_of_vehicle_id_idx PRIMARY KEY (id_register)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.historial_of_vehicle
    OWNER to postgres;

-- Index: historial_event_btree_code

-- DROP INDEX IF EXISTS operational.historial_event_btree_code;

CREATE INDEX IF NOT EXISTS historial_event_btree_code
    ON operational.historial_event USING btree
    (id_internal ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.city
    CLUSTER ON historial_event_btree_code;