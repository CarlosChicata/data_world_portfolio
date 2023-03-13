-- Table: operational.request_of_driver

-- DROP TABLE IF EXISTS operational.request_of_driver;

CREATE TABLE IF NOT EXISTS operational.request_of_driver
(
    request_id integer NOT NULL,
    driver_id integer NOT NULL,
    CONSTRAINT request_of_driver_driver_id FOREIGN KEY (driver_id)
        REFERENCES operational.driver (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT request_of_driver_request_id FOREIGN KEY (request_id)
        REFERENCES operational.request (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.request_of_driver
    OWNER to postgres;
