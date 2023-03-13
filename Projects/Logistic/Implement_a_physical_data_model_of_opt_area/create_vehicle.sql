-- Table: operational.vehicle

-- DROP TABLE IF EXISTS operational.vehicle;

CREATE TABLE IF NOT EXISTS operational.vehicle
(
    plate character varying COLLATE pg_catalog."default" NOT NULL,
    type operational.vehicle_type NOT NULL,
    status operational.vehicle_status NOT NULL,
    "who_Is_owner" operational.owner NOT NULL,
    id integer NOT NULL DEFAULT nextval('operational.vehicle_id_seq'::regclass),
    is_delete boolean NOT NULL,
    city_id integer NOT NULL,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT vehicle_id_idx PRIMARY KEY (id),
    CONSTRAINT vehice_city_id FOREIGN KEY (city_id)
        REFERENCES operational.city (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.vehicle
    OWNER to postgres;