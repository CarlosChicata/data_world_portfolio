-- Table: operational.vehicle

-- DROP TABLE IF EXISTS operational.vehicle;

CREATE TABLE IF NOT EXISTS operational.vehicle
(
    plate character varying COLLATE pg_catalog."default" NOT NULL,
    type operational.vehicle_type NOT NULL,
    status operational.vehicle_status NOT NULL,
    who_is_owner operational.owner NOT NULL,
    id_register integer NOT NULL,
    city_id integer NOT NULL,
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    CONSTRAINT vehicle_id_idx PRIMARY KEY (id_register),
    CONSTRAINT vehice_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.vehicle
    OWNER to postgres;