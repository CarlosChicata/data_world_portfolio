-- Type: change_shipment

-- DROP TYPE IF EXISTS operational.change_shipment;

CREATE TYPE operational.change_shipment AS
(
	previos_value text NOT NULL COLLATE pg_catalog."default",
	current_value text NOT NULL COLLATE pg_catalog."default",
	is_delete boolean,
	operation operational.operation_change_shipment,
	"position" text
);

ALTER TYPE operational.change_shipment
    OWNER TO postgres;