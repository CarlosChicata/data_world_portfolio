-- Table: operational.status_event_route

-- DROP TABLE IF EXISTS operational.status_event_route;

CREATE TABLE IF NOT EXISTS operational.status_event_route
(
    id integer NOT NULL DEFAULT nextval('operational.status_event_route_id_seq'::regclass),
    creation timestamp without time zone NOT NULL DEFAULT now(),
    status operational.route_status NOT NULL,
    is_delete boolean NOT NULL DEFAULT false,
    route_id integer NOT NULL,
    created_user_type operational.created_user_type NOT NULL,
    CONSTRAINT status_event_route_id_idx PRIMARY KEY (id),
    CONSTRAINT status_event_route_route_id FOREIGN KEY (route_id)
        REFERENCES operational.route (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.status_event_route
    OWNER to postgres;