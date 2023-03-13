-- Type: branch_schedule

-- DROP TYPE IF EXISTS operational.branch_schedule;

CREATE TYPE operational.branch_schedule AS
(
	open_time time without time zone,
	close_time time without time zone,
	days operational.days[]
);

ALTER TYPE operational.branch_schedule
    OWNER TO postgres;
