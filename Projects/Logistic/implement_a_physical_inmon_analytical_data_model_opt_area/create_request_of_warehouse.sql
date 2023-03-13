-- Table: operational.request_of_warehouse

-- DROP TABLE IF EXISTS operational.request_of_warehouse;

CREATE TABLE IF NOT EXISTS operational.request_of_warehouse
(
    request_id integer NOT NULL,
    warehouse_id integer NOT NULL,
    CONSTRAINT request_of_warehouse_warehouse_id FOREIGN KEY (warehouse_id)
        REFERENCES operational.warehouse (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT request_of_warehouse_request_id FOREIGN KEY (request_id)
        REFERENCES operational.request (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.request_of_warehouse
    OWNER to postgres;
